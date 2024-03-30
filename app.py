from flask import Flask,request,render_template

from src.mlproject.pipelines.predction_pipeline import PredictPipeline, CustomData

app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("form.html")
    else:
        data=CustomData(
            carat=int(request.form.get("Nitrogen")),
            depth=int(request.form.get("Phosphorous")),
            table=int(request.form.get("Potassium")),
            x=float(request.form.get("temperature")),
            y=float(request.form.get("humidity")),
            z=float(request.form.get("ph")),
            cut=float(request.form.get("rainfall")),
        )
        final_data=data.get_data_as_dataframe()

        predict_pipeline=PredictPipeline()

        pred=predict_pipeline.predict(final_data)

        result={20:"rice", 11:"maize", 8:"jute", 6:"cotton", 4:"coconut", 17:"papaya", 16:"orange", 0:"apple", 15:"muskmelon", 21:"watermelon", 7:"grapes", 12:"mango", 1:"banana", 19:"pomegranate", 10:"lentil", 2:"blackgram", 14:"mungbean",13:"mothbeans",18:"pigeonpeas",9:"kidneybeans",3:"chickpea",5:"coffee"}

        return render_template("result.html",final_result=str(result[pred]))



if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)