# # 




# import os
# import joblib
# from flask import Flask, render_template, request

# app = Flask(__name__)

# models = {}
# for file in os.listdir("groundwater_models"):
#     if file.endswith(".pkl"):
#         key_raw = file.replace("_model", "").replace(".pkl","")
#         key_raw = key_raw.lower()

#         # normalize pre/post monsoon names
#         key = key_raw.replace("premonsoon", "pre_monsoon").replace("postmonsoon", "post_monsoon")

#         models[key] = joblib.load(os.path.join("groundwater_models", file))


# chat_history = []

# @app.route("/", methods=["GET", "POST"])
# def home():
#     global chat_history
#     if request.method == "POST":
#         user_input = request.form["message"]
#         chat_history.append({"sender": "user", "text": user_input})

#         # --- simple parsing (district + season detection) ---
#         msg = user_input.lower()
#         districts = ["buxar", "patna", "gaya", "nalanda"]
#         district = next((d for d in districts if d in msg), None)

#         if "pre" in msg:
#             season = "pre_monsoon"
#         elif "post" in msg:
#             season = "post_monsoon"
#         else:
#             season = None

#         if not district:
#             bot_response = "Sorry, I couldn't detect the district."
#         elif not season:
#             bot_response = "Please specify season: Pre-monsoon or Post-monsoon."
#         else:
#             model_key = f"{district}_{season}"
#             if model_key not in models:
#                 bot_response = f"No model found for {district} ({season})."
#             else:
#                 model = models[model_key]
#                 future = model.make_future_dataframe(periods=6, freq="M")
#                 forecast = model.predict(future)
#                 result = forecast[["ds", "yhat"]].tail(6).to_string(index=False)
#                 bot_response = f"📊 Prediction for {district.title()} ({season.replace('_',' ')})\n{result}"

#         chat_history.append({"sender": "bot", "text": bot_response})

#     return render_template("chatbot.html", chat_history=chat_history)

# if __name__ == "__main__":
#     app.run(debug=True)

# print("Loaded models:", models.keys())


# import os
# import joblib
# import pandas as pd
# import plotly
# import plotly.graph_objs as go
# import json
# from flask import Flask, render_template, request

# app = Flask(__name__)

# # ---------------- Load all models ----------------
# models = {}
# for file in os.listdir("groundwater_models"):
#     if file.endswith(".pkl"):
#         key_raw = file.replace("_model", "").replace(".pkl","").lower()
#         key = key_raw.replace("premonsoon", "pre_monsoon").replace("postmonsoon", "post_monsoon")
#         models[key] = joblib.load(os.path.join("groundwater_models", file))

# print("Loaded models:", models.keys())

# # ---------------- Chat history ----------------
# chat_history = []

# # ---------------- Routes ----------------
# @app.route("/", methods=["GET","POST"])
# def home():
#     global chat_history
#     graphJSON = None

#     if request.method == "POST":
#         user_input = request.form["message"]
#         chat_history.append({"sender": "user", "text": user_input})

#         msg = user_input.lower()

#         # Detect district
#         districts = [d.split("_")[0] for d in models.keys()]  # first part of model key
#         district = next((d for d in districts if d in msg), None)

#         # Detect season
#         if "pre" in msg:
#             season = "pre_monsoon"
#         elif "post" in msg:
#             season = "post_monsoon"
#         else:
#             season = None

#         # Validate
#         if not district:
#             bot_response = "Sorry, I couldn't detect the district."
#         elif not season:
#             bot_response = "Please specify season: Pre-monsoon or Post-monsoon."
#         else:
#             model_key = f"{district}_{season}"
#             if model_key not in models:
#                 bot_response = f"No model found for {district.title()} ({season.replace('_',' ')})"
#             else:
#                 model = models[model_key]

#                 # Forecast next 6 months
#                 future = model.make_future_dataframe(periods=6, freq="M")
#                 forecast = model.predict(future)
#                 result = forecast[["ds", "yhat"]].tail(6)

#                 # Text table
#                 table_text = f"📊 Prediction for {district.title()} ({season.replace('_',' ')})\n"
#                 for idx, row in result.iterrows():
#                     table_text += f"{row['ds'].strftime('%b %Y')} : {row['yhat']:.2f}\n"
#                 bot_response = table_text

#                 # Plotly chart
#                 fig = go.Figure()
#                 fig.add_trace(go.Scatter(
#                     x=result['ds'],
#                     y=result['yhat'],
#                     mode='lines+markers',
#                     name='Groundwater Level'
#                 ))
#                 fig.update_layout(
#                     title=f"{district.title()} ({season.replace('_',' ')}) Groundwater Forecast",
#                     xaxis_title="Month",
#                     yaxis_title="Predicted Groundwater Level",
#                     template="plotly_white"
#                 )
#                 graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

#         chat_history.append({"sender": "bot", "text": bot_response})

#     return render_template("chatbot.html", chat_history=chat_history, graphJSON=graphJSON)

# if __name__ == "__main__":
#     app.run(debug=True)





# import os
# import joblib
# import pandas as pd
# import plotly
# import plotly.graph_objs as go
# import json
# from flask import Flask, render_template, request

# app = Flask(__name__)

# # ---------------- Load all models ----------------
# models = {}
# for file in os.listdir("groundwater_models"):
#     if file.endswith(".pkl"):
#         key_raw = file.replace("_model", "").replace(".pkl","")
#         key_raw = key_raw.lower()

#         # normalize pre/post monsoon names
#         key = key_raw.replace("premonsoon", "pre_monsoon").replace("postmonsoon", "post_monsoon")

#         models[key] = joblib.load(os.path.join("groundwater_models", file))

# print("Loaded models:", models.keys())

# # ---------------- Chat history ----------------
# chat_history = []

# # ---------------- Routes ----------------
# @app.route("/", methods=["GET","POST"])
# def home():
#     global chat_history
#     graphJSON = None

#     # First load welcome message
#     if not chat_history:
#         chat_history.append({"sender":"bot","text":"💧 Welcome! Type district and season to get groundwater forecast. Example: 'Predict groundwater for Buxar pre monsoon'."})

#     if request.method == "POST":
#         user_input = request.form["message"]
#         chat_history.append({"sender": "user", "text": user_input})

#         msg = user_input.lower()

#         # Detect district dynamically from loaded models
#         districts = [k.split("_")[0] for k in models.keys()]
#         district = next((d for d in districts if d in msg), None)

#         # Detect season
#         if "pre" in msg:
#             season = "pre_monsoon"
#         elif "post" in msg:
#             season = "post_monsoon"
#         else:
#             season = None

#         # Generate bot response
#         if not district:
#             bot_response = "Sorry, I couldn't detect the district."
#         elif not season:
#             bot_response = "Please specify season: Pre-monsoon or Post-monsoon."
#         else:
#             model_key = f"{district}_{season}"
#             if model_key not in models:
#                 bot_response = f"No model found for {district.title()} ({season.replace('_',' ')})"
#             else:
#                 model = models[model_key]

#                 # Forecast next 6 months
#                 future = model.make_future_dataframe(periods=6, freq="M")
#                 forecast = model.predict(future)
#                 result = forecast[["ds", "yhat"]].tail(6)

#                 # Text table
#                 table_text = f"📊 Prediction for {district.title()} ({season.replace('_',' ')})\n"
#                 for idx, row in result.iterrows():
#                     table_text += f"{row['ds'].strftime('%b %Y')} : {row['yhat']:.2f}\n"
#                 bot_response = table_text

#                 # Plotly chart
#                 fig = go.Figure()
#                 fig.add_trace(go.Scatter(
#                     x=result['ds'],
#                     y=result['yhat'],
#                     mode='lines+markers',
#                     name='Groundwater Level'
#                 ))
#                 fig.update_layout(
#                     title=f"{district.title()} ({season.replace('_',' ')}) Groundwater Forecast",
#                     xaxis_title="Month",
#                     yaxis_title="Predicted Groundwater Level",
#                     template="plotly_white"
#                 )
#                 graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

#         chat_history.append({"sender": "bot", "text": bot_response})

#     return render_template("chatbot.html", chat_history=chat_history, graphJSON=graphJSON)

# # ---------------- Run server ----------------
# if __name__ == "__main__":
#     app.run(debug=True)












import os
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- Load all models ----------------
models = {}
for file in os.listdir("groundwater_models"):
    if file.endswith(".pkl"):
        key_raw = file.replace("_model", "").replace(".pkl","").lower()
        key = key_raw.replace("premonsoon", "pre_monsoon").replace("postmonsoon", "post_monsoon")
        models[key] = joblib.load(os.path.join("groundwater_models", file))

print("Loaded models:", models.keys())

# ---------------- Chat history ----------------
chat_history = []

# ---------------- Routes ----------------
@app.route("/", methods=["GET","POST"])
def home():
    global chat_history

    # First load welcome message
    if not chat_history:
        chat_history.append({"sender":"bot","text":"💧 Welcome! Type district and season to get groundwater forecast. Example: 'Predict groundwater for Buxar pre monsoon'."})

    if request.method == "POST":
        user_input = request.form["message"]
        chat_history.append({"sender": "user", "text": user_input})

        msg = user_input.lower()

        # Detect district dynamically from loaded models
        districts = [k.split("_")[0] for k in models.keys()]
        district = next((d for d in districts if d in msg), None)

        # Detect season
        if "pre" in msg:
            season = "pre_monsoon"
        elif "post" in msg:
            season = "post_monsoon"
        else:
            season = None

        # Generate bot response
        if not district:
            bot_response = "Sorry, I couldn't detect the district."
        elif not season:
            bot_response = "Please specify season: Pre-monsoon or Post-monsoon."
        else:
            model_key = f"{district}_{season}"
            if model_key not in models:
                bot_response = f"No model found for {district.title()} ({season.replace('_',' ')})"
            else:
                model = models[model_key]

                # Forecast next 6 months
                future = model.make_future_dataframe(periods=6, freq="M")
                forecast = model.predict(future)
                result = forecast[["ds", "yhat"]].tail(6)

                # Text table
                table_text = f"📊 Prediction for {district.title()} ({season.replace('_',' ')})\n"
                for idx, row in result.iterrows():
                    table_text += f"{row['ds'].strftime('%b %Y')} : {row['yhat']:.2f}\n"
                bot_response = table_text

        chat_history.append({"sender": "bot", "text": bot_response})

    return render_template("chatbot.html", chat_history=chat_history)

# ---------------- Run server ----------------
if __name__ == "__main__":
    app.run(debug=True)
print("Loaded models:", models.keys())