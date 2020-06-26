from flask import Flask, request,render_template
import numpy as np
import math

app = Flask(__name__)


@app.route('/')
def get_home():
    return render_template('home.html')




@app.route('/matrix/', methods=['POST'])
def get_matrix():
    if request.method == 'POST':
        num = request.form.get('num')
        type = request.form.get('type')

        def star(N):
            matrix = np.zeros((N, N))
            n = 0
            m= -1

            for i in matrix:
                matrix[n][m] = 1
                matrix[n][n] = 1
                n +=1
                m = m-1

            return (str(matrix).replace("\n","<br>"))



        def diamond(N):
            matrix = np.zeros((N, N))

            n = math.floor(len(matrix[0])/2)
            m = math.ceil(len(matrix[0])/2)
            for i in range(len(matrix)):
                if i < (math.ceil(len(matrix[0])/2)-1):
                    for j in range(n,m):
                        matrix[i][j] = 1
                        matrix[i][j] = 1
                    n = n -1
                    m += 1
                else:
                    for j in range(n,m):
                        matrix[i][j] = 1
                        matrix[i][j] = 1

                    n +=1
                    m = m -1
            return (str(matrix).replace("\n","<br>"))

        try:
            if (int(num) % 2) == 0:
                return ("Please select an Odd Number")

            elif (int(num) % 2) == 1:

                if (int(type)==1):
                    return (star(int(num)))

                elif (int(type)==2):
                    return (diamond(int(num)))

                else:
                    return ("Wrong Type")
        except:
            return ("Something is Wrong with you Input! Please provide an Odd Integer Number")


    return "Empty"




if __name__ == '__main__':
    app.run(debug=True)
