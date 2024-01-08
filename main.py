"""
Session: 1D01
Group Members: Mykyta Kuznietsov, Mark Hanson,
Due Date: Wednesday, December 6th, 2023
Assignment 4: Interfacing with the Web in Python
Summary:collects data about provices and countries from CBC, CBC international and Windspeaker
Resources Used :
https://pypi.org/project/pycountry/"""


from pycountry import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import request, certifi and sll
from urllib import request
import certifi
import ssl

#functiono that establishes the connection and returns html of the webpage
def connection(url):
    #Done by Mark
    myRequest = request.Request(url)  # Making my Request object
    context = ssl.create_default_context(cafile=certifi.where())
    connect = request.urlopen(myRequest, context=context)
    html = connect.read()
    return html

""" Creating a function called countries() to pass a url through. Then creating a dictionary for the countries, 
after it decodes the HTML, passes it through a for loop using all the country names in pycountry.
for each occurence of a country name in the url the dictionary is updated the country being the key 
and the n being the value. Then lastly it sorts the dictionary based on the keys values
"""

def countries(url):
    #Done by Mark
    countryDict = {}
    html = connection(url)
    content = html.decode()
    for country in pycountry.countries:
        n = content.count(str(country.name))
        countryDict.update({country.name: n})
    sortedDict = dict(reversed(sorted(countryDict.items(),key = lambda x:x[1])))
    return sortedDict


'''#function that counts the amount of each province in the HTML file and returns sorted by value dictionary
 where key is the country and the value is number of times it was mentioned'''
'''Mykyta Kuznietsov's code start'''
def provinceGrab(url):

    provinceDict = {}
    provinces = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"]
    #get the html code
    html = connection(url)
    content = html.decode()
    #go through each province and find out how many times it was mentioned in the news
    for province in provinces:
        n = content.count(province)
        #add province to the dictionary
        provinceDict.update({province.capitalize(): n})
    #sort the dictionary with provinces by amount of times they were mentioned
    sortedDict = dict(reversed(sorted(provinceDict.items(), key = lambda x:x[1])))
    #return sorted dictionary
    return sortedDict

def display(cbc1, cbc2, windspeaker, flag):
    '''Displays'''
    max = 0
    maxcount = ''
# formating the output of the data for provinces and the countries formating in orders of
    #when flag is True, the data will be displayed for the provinces, if False, data will be displayed for the countries
    if flag == True:
        print('{:30}{:<8}{:<9}{:<9}'.format('Province', 'CBC', 'WindS.', 'Total'))
    else:
        print('{:30}{:<8}{:<9}{:<9}'.format('Country', 'CBC', 'WindS.', 'Total'))
    #traverse through the sorted dictionary with provinces/countries
    for value, count in cbc1.items():
        #find the maximum amount of mentions for the provinces and countries in all news
        if count + cbc2[value] + windspeaker[value] > max:
            max = count + cbc2[value] + windspeaker[value]
            maxcount = value
        #print out the province/country, count for each news portal and the total times was mentioned in all news
        print('{:30}{:<8}{:<9}{:<9}'.format(value, count + cbc2[value], windspeaker[value], count + cbc2[value] + windspeaker[value]))
    print('\n')
    if flag == True:
        print(f'The province/territory most in the news is: {maxcount}')
    else:
        print(f'The country most in the news is: {maxcount}')
'''Mykyta Kuznietsov's code end'''

def main():
    #Done by Mark
    """Booting up the program, essentially it is just to make everything look a bit nicer"""
    print('\n')
    print('Program is Booted Up')

    #website links
    cbcNewsUrl = 'https://www.cbc.ca/news'
    cbcworldnewsUrl = 'https://www.cbc.ca/news/world'
    windspeakernewsUrl = 'https://windspeaker.com/news'

    # making variable names for calling the previously made functions
    provinceDictcbc = provinceGrab(cbcNewsUrl)
    provinceDictworld = provinceGrab(cbcworldnewsUrl)
    provinceDictwind = provinceGrab(windspeakernewsUrl)
    countryDictCbc = countries(cbcNewsUrl)
    countryDictWorld = countries(cbcworldnewsUrl)
    countryDictwind = countries(windspeakernewsUrl)
    # displaying the url found data
    display(provinceDictcbc, provinceDictworld, provinceDictwind, True)
    display(countryDictCbc, countryDictWorld, countryDictwind, False)


main()

'''Citations:
 https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
 sorting the dictionary by the values
 
 https://realpython.com/python-web-scraping-practical-introduction/
 to understand the bases of webscraping
 
 https://eclass.srv.ualberta.ca/pluginfile.php/10524787/mod_resource/content/0/urllibAsn.py
 We also used the example in the class notes and the notes themselves'''
