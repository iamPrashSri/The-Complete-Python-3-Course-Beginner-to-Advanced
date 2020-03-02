import web

# Setup Routes
urls = (
    '/(.*)/(.*)', 'Index'
)

render = web.template.render('AdvancedPythonConcepts/WebProject/resources/')  # To tell Python where to look for template files
app = web.application(urls, globals())

class Index:
    def GET(self, name, age):
        return render.main(name, age)


if __name__ == '__main__':
    app.run()
