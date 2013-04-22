#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users

class Intern(db.Model):
  name = db.StringProperty()
  dept = db.StringProperty()
  internship_year = db.StringProperty()
  webmail_id = db.StringProperty()
  portfolio_link = db.StringProperty()
  category = db.StringProperty()
  univ_comp = db.StringProperty()
  location = db.StringProperty()
  duration = db.StringProperty()
  when_to_apply = db.StringProperty()
  intern_detail = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<a href="/search">Search for internships </br></a>')
        self.response.write('<a href="/fill">Fill your internship experience</a>')      
        self.response.out.write('<html><body>')
        
        entries = Intern.all()

        self.response.out.write("""
          <table border="1">
            <tr>
              <th>Name</th>
              <th>Department</th>
              <th>Internship Year</th>
              <th>Webmail ID</th>
              <th>Portfolio Link</th>
              <th>Intern Category</th>
              <th>University/Company</th>
              <th>Location</th>
              <th>Duration</th>
              <th>When to apply</th>
              <th>Experience</th>
            </tr>""")

        for i in entries :
            self.response.out.write(
                """<tr>
                    <td>%s</td>""" % i.name)
            self.response.out.write('<td>%s</td>' % i.dept)
            self.response.out.write('<td>%s</td>' % i.internship_year)
            self.response.out.write('<td>%s</td>' % i.webmail_id)
            self.response.out.write('<td>%s</td>' % i.portfolio_link)
            self.response.out.write('<td>%s</td>' % i.category)
            self.response.out.write('<td>%s</td>' % i.univ_comp)
            self.response.out.write('<td>%s</td>' % i.location)
            self.response.out.write('<td>%s</td>' % i.duration)
            self.response.out.write('<td>%s</td>' % i.when_to_apply)
            self.response.out.write('<td>%s</td></tr>' % i.intern_detail)

        self.response.out.write("""</table>
                            </body>
                        </html>""")

class Data(webapp2.RequestHandler):
  def post(self):

    i=Intern()
    i.name = self.request.get('name')
    i.dept = self.request.get('dept')
    i.internship_year = self.request.get('internship_year')
    i.webmail_id = self.request.get('webmail_id')
    i.portfolio_link = self.request.get('portfolio_link')
    i.category = self.request.get('category')
    i.univ_comp = self.request.get('univ_comp')
    i.location = self.request.get('location')
    i.duration = self.request.get('duration')
    i.when_to_apply = self.request.get('when_to_apply')
    i.intern_detail = self.request.get('intern_detail')
    i.put()
            
    self.redirect('/')

class Result(webapp2.RequestHandler):
    def get(self):
        r = Intern.all()
        r.filter("dept =",self.request.get('dept'))
        entries=r.fetch(100)

        self.response.out.write("""
          <table border="1">
            <tr>
              <th>Name</th>
              <th>Department</th>
              <th>Internship Year</th>
              <th>Webmail ID</th>
              <th>Portfolio Link</th>
              <th>Intern Category</th>
              <th>University/Company</th>
              <th>Location</th>
              <th>Duration</th>
              <th>When to apply</th>
              <th>Experience</th>
            </tr>""")

        for i in entries :
            self.response.out.write('<tr><td>%s</td>' % i.name)
            self.response.out.write('<td>%s</td>' % i.dept)
            self.response.out.write('<td>%s</td>' % i.internship_year)
            self.response.out.write('<td>%s</td>' % i.webmail_id)
            self.response.out.write('<td>%s</td>' % i.portfolio_link)
            self.response.out.write('<td>%s</td>' % i.category)
            self.response.out.write('<td>%s</td>' % i.univ_comp)
            self.response.out.write('<td>%s</td>' % i.location)
            self.response.out.write('<td>%s</td>' % i.duration)
            self.response.out.write('<td>%s</td>' % i.when_to_apply)
            self.response.out.write('<td>%s</td></tr>' % i.intern_detail)

        self.response.out.write("""</table>
                            </body>
                        </html>""")

        

class Search(webapp2.RequestHandler):
	def get(self):
		if 1:
			greeting = ("Welcome, <form method='get' action='result'>Dept. Search: <input type='text' name='dept' /><br> User Search : <input type='text' name='user' /><br><input type='submit' value='Submit'></form>")
		else:
			greeting = ("<a href=\"%s\">sign in or register</a>." % users.create_login_url("/new"))
		self.response.out.write("<html><body>%s</body></html>" % greeting)
      

class Fill(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
<html>
<body>
<form action="/sign" method=post>
<fieldset>
<legend>PERSONAL INFORMATION:</legend>
Name: <input name ="name" type="text" size="30" /><br/><br/>
Department:<select name="dept">
<option value="cse">CSE</option>
<option value="ece">ECE</option>
<option value="me">ME</option>
<option value="eee">EEE</option>
<option value="ce">CE</option>
<option value="bt">BT</option>
<option value="cst">CST</option>
<option value="ep">EP</option>
<option value="mnc">MnC</option>
<option value="dod">DOD</option>
</select></br><br/>
Internship Year: <input name="internship_year" type="text" size="30" /><br /><br/>
Webmail ID : <input name="webmail_id" type="text" size="30"><br /><br/>
Portfolio Link : <input name="portfolio_link" type="text" size=30><br /><br/>
</fieldset></br><br/>
<fieldset>
<legend>INTERNSHIP INFORMATION:</legend>
Category:<select name="category">
<option value="Research">Research</option>
<option value="Industrial">Industrial</option>
</select></br><br/>
University/Company: <input name="univ_comp" type="text" size="30" /><br /><br/>
Location: <input name="location" type="text" size="30" /><br /><br/>
Duration: <input name="duration" type="text" size="30"><br /><br/>
</fieldset></br><br/>
<fieldset>
<legend>EXPERIENCE&SUGGESTIONS:</legend>
</textarea></br>
When to Apply: <input name="when_to_apply" type="text" size="40" /><br /><br/>
Experience:</br>
<textarea name="intern_detail" cols="25" rows="5">
</textarea></br>
</fieldset>
<input type="submit" value="Submit" />
</form>
</body>
</html>""")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign', Data),
    ('/result', Result),
    ('/search', Search),
    ('/fill', Fill)
], debug=True)
