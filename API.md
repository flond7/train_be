# CLASS views

## list
class videoList(generics.ListAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

## detail
class videoDetail(generics.RetrieveAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

## create
class videoCreate(generics.CreateAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

  """ HOOK TO ADD IMPLICIT INFORMATION that are not sent with the data by the user
  def perform_create(self, serializer):
    serializer.save(user=self.request.user) """

## update
""" send the object with the key: values you want to change """
class videoUpdate(generics.UpdateAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer
  lookup_field = 'pk'

"""  HOOK TO ADD ACTIONS, such us sending a confirmation email to the user
  def perform_update(self, serializer):
    instance = serializer.save() """