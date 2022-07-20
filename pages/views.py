from django.http import HttpResponse


def homePageView(request):
    response = HttpResponse()
    response.write("<p>Here's the text of the web page.</p>")                                    
    response.write("<p>Your mama is dirty slut.</p>")                                    
    response.write("<p>And everyone knows about it.</p>")                                    
    return response