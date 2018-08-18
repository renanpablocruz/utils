import random
import uuid
import argparse

# adid                | uuid                        |           | not null |
# app_id              | text                        |           | not null |
# campaign            | text                        |           |          |
# source              | text                        |           | not null |
# platform            | text                        |           |          |
# source_app          | text                        |           |          |

APP_IDS = ['my-game01', 'my-game02', 'my-game03']
CAMPAINGS = {'adnet-A' : ['campaign-A-01', 'campaign-A-02', 'campaign-A-03'],
             'adnet-B' : ['campaign-B-01', 'campaign-B-02', 'campaign-B-03']}
SOURCES = ['adnet-A', 'adnet-B']
PLATFORMS = ['android', 'ios']
SOURCE_APPS = ['not-my-game-01', 'not-my-game-02', 'not-my-game-03', 'not-my-game-04', 'not-my-game-05', 'not-my-game-06', 'not-my-game-07', 'not-my-game-08']
COUNTRIES = ['us', 'cn']
VERSIONS = {'my-game01' : ['1.0', '1.1'],
            'my-game02' : ['2.0', '2.1'],
            'my-game03' : ['3.0', '3.1']}

def _click_gen():
  adid = uuid.uuid4()
  app_id = random.choice(APP_IDS)
  source = random.choice(SOURCES)
  campaign = random.choice(CAMPAINGS[source])
  platform = random.choice(PLATFORMS)
  source_app = random.choice(SOURCE_APPS)
  country = random.choice(COUNTRIES)
  timestamp = 1533081600 + random.randint(0, 60*60*24*30)
  return {
        'adid' : adid,
        'app_id' : app_id,
        'source' : source,
        'campaign' : campaign,
        'platform' : platform,
        'source_app' : source_app,
        'country' : country,
        'timestamp' : timestamp
  }

def clicks_generator(n):
  r = []
  for i in range(n):
    r.append(_click_gen())
  return r

def _impression_gen(): # same as click!!!
  adid = uuid.uuid4()
  app_id = random.choice(APP_IDS)
  source = random.choice(SOURCES)
  campaign = random.choice(CAMPAINGS[source])
  platform = random.choice(PLATFORMS)
  source_app = random.choice(SOURCE_APPS)
  country = random.choice(COUNTRIES)
  timestamp = 1533081600 + random.randint(0, 60*60*24*30)
  return {
        'adid' : adid,
        'app_id' : app_id,
        'source' : source,
        'campaign' : campaign,
        'platform' : platform,
        'source_app' : source_app,
        'country' : country,
        'timestamp' : timestamp
  }

def impressions_generator(n):
  r = []
  for i in range(n):
    r.append(_impression_gen())
  return r

def _install_gen():
  adid = uuid.uuid4()
  app_id = random.choice(APP_IDS)
  version = random.choice(VERSIONS[app_id])
  platform = random.choice(PLATFORMS)
  country = random.choice(COUNTRIES)
  timestamp = 1533081600 + random.randint(0, 60*60*24*30)
  return {
        'adid' : adid,
        'app_id' : app_id,
        'platform' : platform,
        'country' : country,
        'timestamp' : timestamp
  }

def installs_generator(n):
  r = []
  for i in range(n):
    r.append(_install_gen())
  return r

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-t')
  parser.add_argument('-n')
  args = parser.parse_args()

  method = args.t
  n = int(args.n)
  if method == 'installs':
    r = installs_generator(n)
  elif method == 'clicks':
    r = clicks_generator(n)
  elif method == 'impressions':
    r = impressions_generator(n)

  print r