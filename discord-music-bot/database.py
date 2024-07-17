import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Playlist(Base):
    __tablename__ = 'playlist'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    songs = relationship("Song", back_populates="playlist")

class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)
    playlist_id = Column(Integer, ForeignKey('playlist.id'))
    playlist = relationship("Playlist", back_populates="songs")

class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_playlist(self, name):
        new_playlist = Playlist(name=name)
        self.session.add(new_playlist)
        self.session.commit()

    def add_song_to_playlist(self, playlist_id, title, artist):
        playlist = self.session.query(Playlist).filter_by(id=playlist_id).first()
        if playlist:
            new_song = Song(title=title, artist=artist, playlist_id=playlist_id)
            self.session.add(new_song)
            self.session.commit()

    def get_playlist_songs(self, playlist_id):
        playlist = self.session.query(Playlist).filter_by(id=playlist_id).first()
        if playlist:
            return playlist.songs
        return None

    def remove_song_from_playlist(self, playlist_id, song_id):
        song = self.session.query(Song).filter_by(id=song_id, playlist_id=playlist_id).first()
        if song:
            self.session.delete(song)
            self.session.commit()

    def reorder_playlist(self, playlist_id, song_id, new_position):
        song = self.session.query(Song).filter_by(id=song_id, playlist_id=playlist_id).first()
        if song:
            song_index = self.get_playlist_songs(playlist_id).index(song)
            playlist_songs = self.get_playlist_songs(playlist_id)
            del playlist_songs[song_index]
            playlist_songs.insert(new_position, song)
            for index, song in enumerate(playlist_songs):
                song.id = index + 1
            self.session.commit()

    def get_all_playlists(self):
        return self.session.query(Playlist).all()

    def get_playlist_by_id(self, playlist_id):
        return self.session.query(Playlist).filter_by(id=playlist_id).first()

    def delete_playlist(self, playlist_id):
        playlist = self.get_playlist_by_id(playlist_id)
        if playlist:
            self.session.delete(playlist)
            self.session.commit()

    def close(self):
        self.session.close()