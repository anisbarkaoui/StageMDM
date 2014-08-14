#!/usr/bin/env python


# ------------------------    Import    --------------------------

import web
import os.path
from libcloud.compute.base import NodeAuthSSHKey
from libcloud.compute.providers import set_driver
from libcloud.compute.providers import get_driver
import stratuslab.libcloud.compute_driver

# ----------------------   URL Dispatcher   -----------------------

urls = (
    '/hadoop', 'list_deployment',
    '/hadoop/(.*)', 'get_deployment'
)



#----------------------     Utilities    -------------------------

# utility to select object by id
def select_id(identifier, objects):
    for o in objects:
        if o.id == identifier:
            return o
    return None


# utility to print id and name of objects
def print_objs(objects):
    str = "\n" + "   ID   |     Name     |   State  |          IP         " + "\n"
    str += "=========================================================" + "\n"
    for o in objects:
        str += '  %s  |   %s   |     %s    |   %s ' % (o.id, o.name, o.state, o.public_ips) + "\n"
    str += "=========================================================" + "\n" + "\n"

    return str


# utility to print status of objects
def print_status(o):
    str = "\n" + "   ID   |     Name     |   State  |          IP         " + "\n"
    str += "=========================================================" + "\n"
    str += '  %s  |   %s   |     %s    |   %s ' % (o.id, o.name, o.state, o.public_ips) + "\n"
    str += "=========================================================" + "\n" + "\n"

    return str


#--------------------------------- Service pour L'URL .../node  --------------------------------------------------

class list_deployment:
    def GET(self):
        #GET list of active virtual machines


        StratusLabDriver = get_driver('stratuslab')
        driver = StratusLabDriver('unused-key')

        ws = print_objs(driver.list_nodes())
        return "<html><body><pre>" + ws + "</pre></body></html>"


    #-----------------------------------------------------------------

    def POST(self):
        StratusLabDriver = get_driver('stratuslab')
        driver = StratusLabDriver('unused-key')



        locations = driver.list_locations()
        location = select_id('grnet', locations)

        images = driver.list_images()
        image = select_id('L5D9_WONgduc_0vkoF8JmGegUDx', images)

        sizes = driver.list_sizes()
        size = select_id('m1.large', sizes)
        vars = web.input()
        size.cpu = vars.cpu
        size.ram = vars.ram


        #--------------------  Get  ssh  key  -------------------------
        home = os.path.expanduser('~')
        ssh_public_key_path = os.path.join(home, '.ssh', 'id_rsa.pub')
        ssh_private_key_path = ssh_public_key_path.rstrip('.pub')
        with open(ssh_public_key_path) as f:
            pubkey = NodeAuthSSHKey(f.read())





        #-----------------Call  Create  Node  -----------------------
        node = driver.create_node(size=size,
                                  location=location,
                                  image=image,
                                  auth=pubkey)

        ws = print_objs(driver.list_nodes())
        return ws


#-----------------------------------  Service  pour URL .../node/id   ----------------------------------------

class get_deployment:

    def GET(self, id):
        StratusLabDriver = get_driver('stratuslab')
        driver = StratusLabDriver('unused-key')

        str = select_id(id, driver.list_nodes())

        ws = print_status(str)
        return ws


        #------------------------

    def DELETE(self, id):
        StratusLabDriver = get_driver('stratuslab')
        driver = StratusLabDriver('unused-key')

        node = select_id(id, driver.list_nodes())
        node.destroy()

        ws = "Node " + id + " is killed ... " + "\n" + "\n"
        return ws  #---------------------------------------------------------------------

if __name__ == "__main__":
    print "DEBUG GOT HERE !!!"
    set_driver('stratuslab', 'stratuslab.libcloud.compute_driver', 'StratusLabNodeDriver')

    app = web.application(urls, globals())
    app.run()

