#!/usr/bin/env python
import web





urls = (
    '/hadoop', 'list_deployment',
    '/hadoop/(.*)', 'get_deployment'
)


class list_deployment:        
    def GET(self):
        ws="call libcloud decribe method"+ "\n"
        return ws


    def POST(self):
	data = web.data() # you can get data use this method
        vars=web.input()
 	ws="data: "+data+ "\n"
	ws+=str(vars)+"\n"
        ws+=vars.name+"\n"
        ws+=vars.lab+"\n"
        ws+=vars.other+"\n"
        return ws

class get_deployment:
    def GET(self, deploy):
	ws="call libcloud decribe method with num_deploy"+deploy+ "\n"
	return ws

    def DELETE(self, deploy):
        ws="call libcloud kill method with num_deploy"+deploy+ "\n"
        return ws



app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

