'''
Stephen Mandelbaum 10-29-2018
suggestion: chmod +x this file and copy it to /usr/bin (you may have to be admin) then you can google straight from the command line!
'''
#!/usr/bin/python3
import webbrowser
import sys
req = webbrowser.open('http://www.google.com/search?q='+''.join(sys.argv[1:]))
