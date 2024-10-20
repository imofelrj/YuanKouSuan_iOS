import mitmproxy

def response(flow):
    if "https://xyks.yuanfudao.com/leo-game-pk/iphone/math/pk/match/v2?pointId" in flow.request.pretty_url:
        with open("response","wb") as f:
                f.write(flow.response.content)