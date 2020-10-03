from bot.config import create_api


# Test whether the API gets created correctly
def test_create_api():
    api = create_api()
    assert api.me().screen_name == "hutsbot"
