import os
import random
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ===== .env から環境変数を読み込む =====
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    print("⚠️ エラー: .env ファイルに CLIENT_ID と CLIENT_SECRET を設定してください。")
    exit()

# ===== Spotify API 認証 =====
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# ===== 人気アーティスト一覧 =====
artists = ["YOASOBI", "Ado", "Official髭男dism", "King Gnu", "Vaundy", "米津玄師"]
artist_name = random.choice(artists)

print(f"\n🎵 アーティスト「{artist_name}」からランダムに曲を選びます...\n")

# ===== 曲データを取得 =====
results = sp.search(q=f'artist:{artist_name}', type='track', limit=10)
tracks = results['tracks']['items']

if not tracks:
    print("⚠️ 曲が見つかりませんでした。もう一度試してください。")
    exit()

# ===== ランダムに1曲選ぶ =====
track = random.choice(tracks)

track_name = track['name']
album_name = track['album']['name']
release_date = track['album']['release_date']
popularity = track['popularity']

# ===== クイズヒントを表示 =====
print("🧩 ヒントはこちら：")
print(f"・アーティスト：{artist_name}")
print(f"・アルバム名：{album_name}")
print(f"・リリース日：{release_date}")
print(f"・人気度（0〜100）：{popularity}")
print(f"・Spotify URL：{track['external_urls']['spotify']}")
print("-" * 40)

# ===== 回答 =====
answer = input("❓ この曲のタイトルは？：")

if answer.strip().lower() in track_name.lower():
    print("🎉 正解！すごい！")
else:
    print(f"❌ 残念！正解は「{track_name}」でした！")

print("\n👉 聴いてみたい人はこちら：", track['external_urls']['spotify'])
