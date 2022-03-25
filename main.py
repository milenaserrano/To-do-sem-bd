from flask import Flask, render_template, request, redirect
app = Flask('app')

# flask = criar o programinha
# render_template = renderizar
# request = receber requisiçoes
# redirect = redirecionar o usuario pra outra rota



todos = [
  
  { 'title': 'Estudar python' },
  { 'title': 'Estudar JavaScript'}
]

@app.route('/')
def index():
  return render_template('index.html', todos=todos)



@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('title')
  todos.append({'title': title})
  return redirect('/')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)