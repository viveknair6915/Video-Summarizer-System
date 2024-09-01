import random

class Misc:
    @staticmethod
    def loaderx():
        loader = [
            "🔄 Loading...",
            "⏳ Summarizer is brewing your content potion...",
            "🌟 The Summarizer is working its magic...",
            "🤖 Processing your request..."
        ]
        return random.choice(loader)

    @staticmethod  
    def footer():
        ft = """
        <style>
        a:link, a:visited {
            color: #BFBFBF;
            background-color: transparent;
            text-decoration: none;
        }

        a:hover, a:active {
            color: #0283C3;
            background-color: transparent;
            text-decoration: underline;
        }

        #page-container {
            position: relative;
            min-height: 10vh;
        }

        .footer {
            position: relative;
            width: 100%;
            background-color: transparent;
            color: #808080;
            text-align: center;
            padding: 10px 0;
            font-size: 0.875em;
        }
        </style>

        <div id="page-container">
            <div class="footer">
                <p>By <a href="https://github.com/viveknair6915" target="_blank">Vivek V Nair</a></p>
            </div>
        </div>
        """
        return ft
