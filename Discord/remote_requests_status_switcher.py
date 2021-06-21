from flask import Flask
app = Flask(__name__.split('.')[0])


@app.route('/')
def home():
    return "You are at the homepage!"

@app.route('/ok/<token>')
def ok(token):
    return '''
<!DOCTYPE Html>
<html>
    <head>

    </head>
    <body>
        <button id="ok">Ok</button>
        <script>
            document.getElementById("ok").onclick = function() {
                const statuses = [
                    "Drunk",
                    "Sleeping, idk",
                    "I luv u",
                    "Coding is cool",
                    "School in the US is flawed. Except for Montessori, perhaps",
                    "Minecraft is the best video game",
                    "In space",
                    "Let us rule the world and take over China",
                    "Watching Clone Wars",
                    "Developing my Discord Bot",
                    "Oh, my goodness no!",
                    "ReEEEEeEeEEEeeEeeeEEE",
                    "Brainstorming...",
                    "Difficult Minecraft builds",
                    "Who you once were does not have to define who you are now",
                    "Ahsoka pog",
                    "I should be sleeping",
                    "Plush F.A.O Schwarz Monkeys for everyone!",
                    "Long list of statuses",
                    "Cozy development corner"
                ]
                let authtoken = "''' + token + '''";
                let content_type = "application/json";



                setInterval(function() {
                    let request = new XMLHttpRequest();
                    let url = "https://discord.com/api/v9/users/@me/settings";
                    let data = JSON.stringify({
                        "custom_status": {
                            "text": statuses[Math.floor(Math.random() * 10)]
                        }
                    });
                    let userAgent = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36";
                    

                    request.open("PATCH", url);
                    request.setRequestHeader("authorization", authtoken);
                    request.setRequestHeader("Content-Type", content_type);
                    request.setRequestHeader("User-Agent", userAgent);
                    request.send(data);
                    alert(request.status);
                }, 10000);
            }
        </script>
    </body>
</html>
'''
