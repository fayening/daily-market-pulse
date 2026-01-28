"""Configuration management for Daily Market Pulse."""

import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv


@dataclass
class RedditConfig:
    """Reddit API configuration."""
    client_id: str
    client_secret: str
    user_agent: str
    subreddit: str
    rate_limit: int

    # TODO: Add validation for credentials


@dataclass
class CacheConfig:
    """Cache configuration."""
    expire_time: int

    # TODO: Add cache backend selection (memory/file)


@dataclass
class StorageConfig:
    """Storage configuration."""
    retention_days: int

    # TODO: Add database path configuration


@dataclass
class BackoffConfig:
    """Rate limit backoff configuration."""
    max_retries: int
    base_delay: int

    # TODO: Add exponential backoff parameters


@dataclass
class Config:
    """Main application configuration."""
    reddit: RedditConfig
    cache: CacheConfig
    storage: StorageConfig
    backoff: BackoffConfig
    discord_webhook_url: Optional[str] = None


def load_config() -> Config:
    """
    Load configuration from environment variables.

    Returns:
        Config: Application configuration

    Raises:
        ValueError: If required environment variables are missing
    """
    # TODO: Implement environment variable loading
    # TODO: Validate all required variables are present
    # TODO: Add default values for optional settings
    # TODO: Implement config validation
    pass


def validate_config(config: Config) -> bool:
    """
    Validate configuration values.

    Args:
        config: Configuration to validate

    Returns:
        bool: True if valid

    Raises:
        ValueError: If configuration is invalid
    """
    # TODO: Validate rate limits are within Reddit API guidelines
    # TODO: Validate retention days is >= 1
    # TODO: Validate backoff parameters are reasonable
    pass
