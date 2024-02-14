from urllib.parse import urlencode, quote

def get_url(tweet_Id):
    _url = "https://api.twitter.com/graphql/MWY3AO9_I3rcP_L2A4FR4A/TweetResultByRestId?"
    _dict = {
        "variables": {
            "tweetId":tweet_Id,
            "withCommunity":False,
            "includePromotedContent":False,
            "withVoice":False
        },
        "features": {
            "creator_subscriptions_tweet_preview_api_enabled":True,
            "c9s_tweet_anatomy_moderator_badge_enabled":True,
            "tweetypie_unmention_optimization_enabled":True,
            "responsive_web_edit_tweet_api_enabled":True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled":True,
            "view_counts_everywhere_api_enabled":True,
            "longform_notetweets_consumption_enabled":True,
            "responsive_web_twitter_article_tweet_consumption_enabled":True,
            "tweet_awards_web_tipping_enabled":False,
            "freedom_of_speech_not_reach_fetch_enabled":True,
            "standardized_nudges_misinfo":True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":True,
            "rweb_video_timestamps_enabled":True,
            "longform_notetweets_rich_text_read_enabled":True,
            "longform_notetweets_inline_media_enabled":True,
            "responsive_web_graphql_exclude_directive_enabled":True,
            "verified_phone_label_enabled":False,
            "responsive_web_media_download_video_enabled":True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled":False,
            "responsive_web_graphql_timeline_navigation_enabled":True,
            "responsive_web_enhance_cards_enabled":False
        }
    }

    encoded_parameters = urlencode(_dict, quote_via=quote)
    request_url = _url+encoded_parameters
    request_url = request_url.replace("%20", "").replace("%27", "%22").replace("False", "false").replace("True", "true")
    return request_url