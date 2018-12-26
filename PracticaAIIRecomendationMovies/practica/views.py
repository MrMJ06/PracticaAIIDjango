from django.shortcuts import render
from practica.models import *
import numpy as np


# Create your views here.

# Returns the Pearson correlation coefficient for p1 and p2
# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(p1,p2, type=0):
    if type is 0:
        puntuaciones_p1 = Puntuacion.objects.filter(usuario__id=p1.id)
        #puntuaciones_p2 = Puntuacion.objects.filter(usuario__id=p2.id)
    else:
        puntuaciones_p1 = Puntuacion.objects.filter(pelicula__id=p1.id)
        #puntuaciones_p2 = Puntuacion.objects.filter(pelicula__id=p2.id)

    # Get the list of mutually rated items
    si={}
    for item in puntuaciones_p1:

        if type is 0:
            puntuaciones_p2_pelicula = Puntuacion.objects.filter(usuario__id=p2.id, pelicula__id=item.pelicula.id)
            si.setdefault(item.usuario, ([], []))
        else:
            puntuaciones_p2_pelicula = Puntuacion.objects.filter(usuario__id=item.usuario.id, pelicula__id=p2.id)
            si.setdefault(item.pelicula, ([], []))

        if len(puntuaciones_p2_pelicula) > 0:
            if type == 1:
                si[item.pelicula][0].append(item.puntuacion)
                si[item.pelicula][1].append(puntuaciones_p2_pelicula[0].puntuacion)
            else:
                si[item.usuario][0].append(item.puntuacion)
                si[item.usuario][1].append(puntuaciones_p2_pelicula[0].puntuacion)
        # Find the number of elements
    n=np.minimum(len(si[p1][0]), len(si[p1][1]))

    # if they are no ratings in common, return 0
    if n==0: return 0
    print(si)
    # Add up all the preferences
    sum1=sum(si[p1][0])
    sum2=sum(si[p1][1])
    # Sum up the squares
    sum1Sq=sum([pow(puntuaciones, 2) for puntuaciones in si[p1][0]])
    sum2Sq=sum([pow(puntuaciones, 2) for puntuaciones in si[p1][1]])
    # Sum up the products
    pSum=sum(np.array(si[p1][0])*np.array(si[p1][1]))
    # Calculate Pearson score
    num=pSum-(sum1*sum2/n)
    den=float(np.sqrt(float(sum1Sq-pow(sum1,2)/n)*float(sum2Sq-pow(sum2,2)/n)))
    if den==0: return 0

    r=num/den

    return r


# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(film,n=5,similarity=sim_pearson):
    scores=[(similarity(film,other),other) for other in Pelicula.objects.all() if other.id!=film.id]
    # Sort the list so the highest scores appear at the top
    scores.sort()
    scores.reverse()
    return scores[0:n]


# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in Usuario.objects.all():
        # don't compare me to myself
        if other==person: continue
        sim=similarity(person,other)
        # ignore scores of zero or lower
        if sim<=0: continue
        puntuaciones_otro = Puntuacion.objects.filter(usuario__id=other.id)
        for item in puntuaciones_otro:
            puntuaciones_usuario_pelicula_otro = Puntuacion.objects.filter(usuario__id=person.id, pelicula__id=item.pelicula.id)
            # only score movies I haven't seen yet
            if len(puntuaciones_usuario_pelicula_otro) > 0 or item.puntuacion == 0:
                # Similarity * Score
                totals.setdefault(item.pelicula, 0)
                totals[item.pelicula] += item.puntuacion*sim
                # Sum of similarities
                simSums.setdefault(item.pelicula, 0)
                simSums[item.pelicula] += sim
    print(totals)
    # Create the normalized list
    rankings=[(float(total/simSums[item]), item) for item, total in totals.items()]
    # Return the sorted list
    rankings = sorted(rankings, key= lambda x: x[0], reverse=True)
    #rankings.reverse()
    print(rankings)
    return rankings


def getRecommendedItems(itemMatch):
    scores={}
    # Loop over items rated by this user
    for pelicula in Pelicula.objects.all():
        if pelicula.id == itemMatch.id: continue
        similarity = sim_pearson(itemMatch, pelicula, type=1)
        if similarity == 0 : continue
        # Weighted sum of rating times similarity
        scores.setdefault(pelicula,0)
        scores[pelicula]=similarity
    # Divide each total score by total weighting to get an average
    rankings=[(score, item) for item,score in scores.items( )]
    # Return the rankings from highest to lowest
    rankings = sorted(rankings, key=lambda x: x[0], reverse=True)
    print(rankings)
    return rankings


def calculateSimilarItems(prefs,n=10):
    # Create a dictionary of items showing which other items they
    # are most similar to.
    result={}
    # Invert the preference matrix to be item-centric
    itemPrefs=Pelicula.objects.all()
    c=0
    for item in itemPrefs:
        # Status updates for large datasets
        c+=1
        if c%100==0: print("%d / %d" % (c,len(itemPrefs)))
        # Find the most similar items to this one
        scores=topMatches(itemPrefs, item)
        result[item]=scores

    return result

def recomienda_peliculas_usuario(request, u):

    user = Usuario.objects.filter(id=u)
    recommendations = getRecommendations(user[0])

    return render(request, 'practica/result.html',{'recommendations':recommendations})


def recomienda_peliculas_similares(request, u):

    itemMatch = Pelicula.objects.filter(id=u)
    recommendations = getRecommendedItems(itemMatch[0])

    return render(request, 'practica/result.html',{'recommendations':recommendations})
