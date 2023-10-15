from pydantic import BaseModel
from typing import Optional

class SpreadsSchema(BaseModel):
    Broker: str
    UserId: str
    Date: str
    Symbol: str
    Status: str
    ExpiryDate: str
    ExpiryType: str
    ProductType: str
    Exchange: str
    Segment: str
    TradeType: str
    Trend: str
    Spot_Price: float
    Strike: float
    Leg1_Strike: float
    Leg1_Side: str
    Leg1_Symbol: str
    Leg1_Qty: int
    Leg1_BuyPrice: float
    Leg1_BuyOrderId: int
    Leg1_SellPrice: float
    Leg1_SellOrderId: int
    Leg1_Sl_Price: float
    Leg1_Sl_OrderId: int
    Leg1_Tg_Price: float
    Leg1_Tg_OrderId: int
    Leg1_Pnl: float
    Leg2_Strike: float
    Leg2_Side: str
    Leg2_Symbol: str
    Leg2_Qty: int
    Leg2_BuyPrice: float
    Leg2_BuyOrderId: int
    Leg2_SellPrice: float
    Leg2_SellOrderId: int
    Leg2_Sl_Price: float
    Leg2_Sl_OrderId: int
    Leg2_Tg_Price: float
    Leg2_Tg_OrderId: int
    Leg2_Pnl: float
    Trade_StartTime: str
    Trade_EndTime: str
    Total_Premium: float
    Total_Sl: float
    LastPrice: float
    LastPriceDate: str
    MarketValue: float
    Strategy: str
    Instrument: str
    Pyramid: int
    UnderlyingSymbol: str
    TradeDuration: str
    SpreadNumber: int
    SpreadType: str
    SpreadStatus: str
    Pnl: float
    Charges: float
    PnlNet: float
    Remarks: str

    class Config:
        from_attributes = True


class HedgesSchema(BaseModel):
    Broker: str
    UserId: str
    Date: str
    Symbol: str
    Status: str
    ExpiryDate: str
    ExpiryType: str
    ProductType: str
    Exchange: str
    Segment: str
    OptionType: str
    Spot_Price: float
    Strike: float
    OrderSide: str
    Quantity: int
    BuyPrice: float
    SellPrice: float
    StopLossPrice: float
    StopLossOrderID: float
    TargetPrice: float
    TargetOrderID: float
    Trade_StartTime: str
    Trade_EndTime: str
    LastPrice: float
    LastPriceDate: str
    MarketValue: float
    Strategy: str
    Instrument: str
    UnderlyingSymbol: str
    Pnl: float
    Charges: float
    PnlNet: float
    Remarks: str

    class Config:
        from_attributes = True


class PLDateSummarySchema(BaseModel):
    Broker: str
    UserId: str
    Date: str
    Strategy: str
    Pnl: float
    Charges: float
    PnlNet: float
    TradeType: str
    Brokerage: float
    Slippage: float
    ActualPnl: float
    ActualCharges: float
    ActualPnlNet: float
    ActualBrokerage: float

    class Config:
        from_attributes = True


class PLFundsRiskSchema(BaseModel):
    Broker: str
    UserId: str
    DateTime: str
    StartOfTheDayBalance: float
    AvailableBalance: float
    UtilizedBalance: float
    UtilizationPercentage: float
    UnrealizedProfit: float
    RealizedProfit: float
    PnlAmount: float
    PnlPercentage: float
    RiskAmount: float
    RiskPercentage: float

    class Config:
        from_attributes = True