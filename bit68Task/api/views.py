from django.shortcuts import render
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import permissions
from .serializers import CitySerializer

class WeatherAPI(APIView):
	"""Weather API request by city name by user,return response from  provider with weather data in json format"""
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = CitySerializer
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			city_name 	= serializer.data['city']
			url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=917fe0498a0cf04f95e2814b27d764c8'
			if city_name:
				"""convert weather data to json format"""
				r = requests.get(url.format(city_name)).json()
				try:
					city_weather = {
				            'city' : city_name,
				            'temperature' : r['main']['temp'],
				            'description' : r['weather'][0]['description'],
				            'icon' : r['weather'][0]['icon'],
				        }
					print(city_weather)
					return Response(city_weather)
				except KeyError:
					raise APIException("City Not Found,Please Enter valid City name")
			return Response(self.serializer_class.data)
