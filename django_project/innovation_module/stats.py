import json
import datetime

from . import models, idea, opinion, decision, forum

def get_stats():
    tday = datetime.date.today()
    return json.dumps({
        'ideasCount': idea.count_all(),
        'ideasCountToday': idea.count_date(tday),
        'opinionsCount': opinion.count_all(),
        'opinionsCountToday': opinion.count_date(tday),
        'decisionsCount': decision.count_all(),
        'threadsCount': forum.count_threads_all(),
        'postsCount': forum.count_posts_all()
    })