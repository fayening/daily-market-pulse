"""Stock ticker extraction from text."""

import re
from typing import List, Set, Dict, Any
from collections import Counter


class TickerExtractor:
    """
    Extract stock tickers from Reddit posts and comments.

    Features:
    - Pattern-based extraction
    - Common word filtering (to avoid false positives)
    - Frequency counting
    - Sentiment context extraction
    """

    # Common words that look like tickers but aren't
    EXCLUDED_WORDS = {
        "I", "A", "CEO", "IPO", "DD", "YOLO", "WSB", "IMO", "ETA",
        "US", "USA", "UK", "EU", "ATH", "GDP", "CPI", "FED", "SEC"
    }

    def __init__(self, min_ticker_length: int = 1, max_ticker_length: int = 5):
        """
        Initialize ticker extractor.

        Args:
            min_ticker_length: Minimum ticker symbol length
            max_ticker_length: Maximum ticker symbol length
        """
        # TODO: Initialize regex patterns
        # TODO: Load additional exclusion list if available
        # TODO: Set up validation rules
        pass

    def extract_from_text(self, text: str) -> Set[str]:
        """
        Extract ticker symbols from text.

        Args:
            text: Text content (post title, body, or comment)

        Returns:
            Set of extracted ticker symbols

        Examples:
            >>> extractor = TickerExtractor()
            >>> extractor.extract_from_text("Bullish on $AAPL and $TSLA")
            {'AAPL', 'TSLA'}
        """
        # TODO: Apply regex to find $TICKER patterns
        # TODO: Find UPPERCASE words (potential tickers)
        # TODO: Filter out excluded words
        # TODO: Validate ticker format
        # TODO: Return unique tickers
        pass

    def extract_from_post(self, post: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract tickers from a Reddit post.

        Args:
            post: Post dictionary from RedditClient

        Returns:
            Dictionary with tickers and metadata
            {
                'post_id': str,
                'tickers': List[str],
                'title': str,
                'score': int,
                'num_comments': int,
                'timestamp': datetime
            }
        """
        # TODO: Extract from title
        # TODO: Extract from body text
        # TODO: Combine and deduplicate
        # TODO: Add post metadata
        pass

    def extract_from_comments(self, comments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Extract tickers from comments.

        Args:
            comments: List of comment dictionaries

        Returns:
            List of comment ticker extractions with metadata
        """
        # TODO: Process each comment
        # TODO: Extract tickers from comment body
        # TODO: Add comment metadata (score, timestamp)
        pass

    def count_ticker_mentions(self, extractions: List[Dict[str, Any]]) -> Counter:
        """
        Count ticker mention frequency.

        Args:
            extractions: List of extraction results

        Returns:
            Counter of ticker symbols with counts
        """
        # TODO: Aggregate all tickers
        # TODO: Count frequencies
        # TODO: Sort by count descending
        pass

    def get_ticker_context(self, text: str, ticker: str, window: int = 50) -> str:
        """
        Extract context around ticker mention.

        Args:
            text: Full text
            ticker: Ticker symbol to find
            window: Number of characters before/after ticker

        Returns:
            Text snippet around ticker mention
        """
        # TODO: Find ticker position in text
        # TODO: Extract surrounding context
        # TODO: Handle multiple mentions
        pass
