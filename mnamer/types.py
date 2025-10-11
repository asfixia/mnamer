"""Enum type definitions."""

from __future__ import annotations

from enum import Enum


class MediaType(Enum):
    EPISODE = "episode"
    MOVIE = "movie"

    @classmethod
    def to_media_type(cls) -> type[MediaType]:
        return cls


class MessageType(Enum):
    INFO = None
    ALERT = "yellow"
    ERROR = "red"
    SUCCESS = "green"
    HEADING = "bold"


class ProviderType(Enum):
    TVDB = "tvdb"
    TVMAZE = "tvmaze"
    TMDB = "tmdb"
    OMDB = "omdb"


class RelocateType(Enum):
    MOVE = "move"
    HARDLINK = "hardlink"
    SYMBOLICLINK = "symlink"
    COPY = "copy"
    COPY2 = "copy-with-metadata"
    def get_strategy(self):
        from shutil import move, copy, copy2
        from os import link, symlink
        strategies = {
            RelocateType.MOVE: move,
            RelocateType.HARDLINK: link,
            RelocateType.SYMBOLICLINK: symlink,
            RelocateType.COPY: copy,
            RelocateType.COPY2: copy2,
        }
        return strategies[self]


class SettingType(Enum):
    DIRECTIVE = "directive"
    PARAMETER = "parameter"
    POSITIONAL = "positional"
    CONFIGURATION = "configuration"
