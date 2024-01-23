# counter-service
#USAGE:
docker pull edenmor1989/counter-service 
docker run -d --name counter-service -p 80:80 edenmor1989/counter-service:$(Build.BuildId)

#POST- 
curl -X POST localhost:80
$GET
curl -X GET localhost:80

the number of post requests is updated everytime you do POST request
and then displayed on screen
