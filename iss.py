#!/usr/bin/env python
import requests
import turtle
import time

__author__ = 'peyton glover worked with corbin creech'



def get_astro():
    result = []
    response = requests.get('http://api.open-notify.org/astros.json')
    response = response.json()
    for person in response["people"]:
        result.append(person['name'])
        result.append(person['craft'])
    result.append('total astronauts in space: {}'.format(len(response["people"])))
    print(result)


    
def get_coord():
    result = []
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response = response.json()
    result.append(response["iss_position"])
    result.append('timestamp: {}'.format(response["timestamp"]))
    return result
    print(result)




def get_indy_time():
    location = {'lat':39.7683333, 'lon': -86.1580556}
    response = requests.get('http://api.open-notify.org/iss-pass.json', location)
    response = response.json()
    print(response)
    return response


def do_turtle():
    indytime = get_indy_time()

    screen = turtle.Screen()
    screen.setup(width=720, height=360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('./map.gif')
    screen.screensize(720, 360)
    screen.register_shape('./iss.gif')

    indylat = 39.7683333
    indylon = -86.1580556

    yellowdot = turtle.Turtle()
    yellowdot.penup()
    yellowdot.goto(indylon, indylat)
    yellowdot.dot(10, "yellow")

    coords = get_coord()
    lat = coords[0]['latitude']
    lon = coords[0]['longitude']
    iss = turtle.Turtle()
    iss.penup()
    iss.shape('./iss.gif')
    iss.setheading(90)
    iss.goto(float(lon), float(lat))

    human_time = time.ctime(indytime['response'][0]['risetime'])
    yellowdot.write(str(human_time), align='center', font=("Arial", 12, "bold"))
    
    return screen


def main():
    get_astro()
    get_coord()
    get_indy_time()
    test = do_turtle()
    test.exitonclick()


if __name__ == '__main__':
    main()
