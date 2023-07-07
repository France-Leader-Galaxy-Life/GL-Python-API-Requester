from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class PlayerStatsDTO:
	"""
	Represents the stats of Galaxy Life player.
	"""
	TotalPlayTimeInMs: int
	NpcsAttacked: int
	PlayersAttacked: int
	TimesAttacked: int
	StarbasesDestroyed: int
	BuildingsDestroyed: int
	DamageDoneInAttacks: int
	ObstaclesRecycled: int
	CoinsSpent: int
	MineralsSpent: int
	CoinsFromAttacks: int
	MineralsFromAttacks: int
	ScoreFromAttacks: int
	NukesUsed: int
	TroopsTrained: int
	TroopSizesDonated: int
	FriendsHelped: int
	GiftsReceived: int
	GiftsSent: int
	ColoniesMoved: int
	RivalsWon: int
	ChipsWonFromRivals: int
