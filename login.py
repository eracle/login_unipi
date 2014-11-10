import mechanize



username='username'
password='password'


br = mechanize.Browser()

agentHeader = [("User agent","(X11; U; Linux x86_64; en-US; rv:1.8.1.14) Gecko/20080418 Ubuntu/8.04 (hardy) Firefox/2.0.0.14")]
br.addheaders = agentHeader
br.set_handle_robots(False)
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


br.set_handle_equiv(True)
br.set_handle_referer(True)
# Turn on debugging messages
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)


#br.set_handle_equiv(False)

page = br.open("http://www.gstatic.com/generate_204")
#data = br.submit()
br.open(page.geturl())



br.select_form(name='loginform')
br.form['username'] = username
br.form['password'] = password

data = br.submit()

