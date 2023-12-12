from django.http import JsonResponse
import joblib
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
import pandas as pd

@api_view(['POST'])
def knn_Dropped(request):
    if request.method == 'POST':
        try:
             # Load your .pkl file
            model = joblib.load(r'C:\Users\cher_karim\Desktop\5eme\AI\project\Models\knnDropped.pkl')

            # Access data from the request
            uploaded_file = request.FILES['dataset']
            df = pd.read_excel(uploaded_file)
            features = np.array(df[['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength', 'AspectRation',
                                         'Eccentricity', 'ConvexArea', 'EquivDiameter', 'Extent', 'Solidity',
                                         'roundness', 'Compactness', 'ShapeFactor1', 'ShapeFactor2', 'ShapeFactor3', 'ShapeFactor4']])
            
            # Perform any necessary processing using the loaded model
            prediction = model.predict(features)

            # Return the response
            return JsonResponse({'prediction': prediction.tolist()})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def knn_Frequent(request):
    if request.method == 'POST':
        try:
             # Load your .pkl file
            model = joblib.load(r'C:\Users\cher_karim\Desktop\5eme\AI\project\Models\knnFrequent.pkl')

            # Access data from the request
            uploaded_file = request.FILES['dataset']
            df = pd.read_excel(uploaded_file)
            features = np.array(df[['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength', 'AspectRation',
                                         'Eccentricity', 'ConvexArea', 'EquivDiameter', 'Extent', 'Solidity',
                                         'roundness', 'Compactness', 'ShapeFactor1', 'ShapeFactor2', 'ShapeFactor3', 'ShapeFactor4']])
            
            # Perform any necessary processing using the loaded model
            prediction = model.predict(features)

            # Return the response
            return JsonResponse({'prediction': prediction.tolist()})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def kmeans_Dropped(request):
    if request.method == 'POST':
        try:
             # Load your .pkl file
            model = joblib.load(r'C:\Users\cher_karim\Desktop\5eme\AI\project\Models\kmeansDropped.pkl')
            uploaded_file = request.FILES['dataset']
            df = pd.read_excel(uploaded_file)
            features = np.array(df[['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength', 'AspectRation',
                                         'Eccentricity', 'ConvexArea', 'EquivDiameter', 'Extent', 'Solidity',
                                         'roundness', 'Compactness', 'ShapeFactor1', 'ShapeFactor2', 'ShapeFactor3', 'ShapeFactor4']])
            
            prediction = model.predict(features)


            return JsonResponse({'prediction': prediction.tolist()})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def kmeans_Frequent(request):
    if request.method == 'POST':
        try:
             # Load your .pkl file
            model = joblib.load(r'C:\Users\cher_karim\Desktop\5eme\AI\project\Models\kmeansFrequent.pkl')

            # Access data from the request
            uploaded_file = request.FILES['dataset']
            df = pd.read_excel(uploaded_file)
            features = np.array(df[['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength', 'AspectRation',
                                         'Eccentricity', 'ConvexArea', 'EquivDiameter', 'Extent', 'Solidity',
                                         'roundness', 'Compactness', 'ShapeFactor1', 'ShapeFactor2', 'ShapeFactor3', 'ShapeFactor4']])
            

            # Perform any necessary processing using the loaded model
            prediction = model.predict(features)

            # Return the response
            return JsonResponse({'prediction': prediction.tolist()})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)
