from pydantic import BaseModel
from typing import Optional

class ResponseSchema(BaseModel):
    status:str
    code:str
    description: str
    data:list

class SpreadsSchemaIn(BaseModel):
    Broker: str
    UserId: str
    Date: Optional[str] = None
    Symbol: Optional[str] = None
    Status: Optional[str] = None
    ExpiryDate: Optional[str] = None
    ExpiryType: Optional[str] = None
    ProductType: Optional[str] = None
    Exchange: Optional[str] = None
    Segment: Optional[str] = None
    TradeType: Optional[str] = None
    Trend: Optional[str] = None
    Spot_Price: Optional[float] = None
    Strike: Optional[float] = None
    Leg1_Strike: Optional[float] = None
    Leg1_Side: Optional[str] = None
    Leg1_Symbol: Optional[str] = None
    Leg1_Qty: Optional[int] = None
    Leg1_BuyPrice: Optional[float] = None
    Leg1_BuyOrderId: Optional[int] = None
    Leg1_SellPrice: Optional[float] = None
    Leg1_SellOrderId: Optional[int] = None
    Leg1_Sl_Price: Optional[float] = None
    Leg1_Sl_OrderId: Optional[int] = None
    Leg1_Tg_Price: Optional[float] = None
    Leg1_Tg_OrderId: Optional[int] = None
    Leg1_Pnl: Optional[float] = None
    Leg2_Strike: Optional[float] = None
    Leg2_Side: Optional[str] = None
    Leg2_Symbol: Optional[str] = None
    Leg2_Qty: Optional[int] = None
    Leg2_BuyPrice: Optional[float] = None
    Leg2_BuyOrderId: Optional[int] = None
    Leg2_SellPrice: Optional[float] = None
    Leg2_SellOrderId: Optional[int] = None
    Leg2_Sl_Price: Optional[float] = None
    Leg2_Sl_OrderId: Optional[int] = None
    Leg2_Tg_Price: Optional[float] = None
    Leg2_Tg_OrderId: Optional[int] = None
    Leg2_Pnl: Optional[float] = None
    Trade_StartTime: Optional[str] = None
    Trade_EndTime: Optional[str] = None
    Total_Premium: Optional[float] = None
    Total_Sl: Optional[float] = None
    LastPrice: Optional[float] = None
    LastPriceDate: Optional[str] = None
    MarketValue: Optional[float] = None
    Strategy: Optional[str] = None
    Instrument: Optional[str] = None
    Pyramid: Optional[int] = None
    UnderlyingSymbol: Optional[str] = None
    TradeDuration: Optional[str] = None
    SpreadNumber: Optional[int] = None
    SpreadType: Optional[str] = None
    SpreadStatus: Optional[str] = None
    Pnl: Optional[float] = None
    Charges: float
    PnlNet: Optional[float] = None
    Remarks: Optional[str] = None

    class Config:
        from_attributes = True

class SpreadsSchemaOut(BaseModel):
    SpreadId: int
    Broker: str
    UserId: str
    Date: Optional[str] = None
    Symbol: Optional[str] = None
    Status: Optional[str] = None
    ExpiryDate: Optional[str] = None
    ExpiryType: Optional[str] = None
    ProductType: Optional[str] = None
    Exchange: Optional[str] = None
    Segment: Optional[str] = None
    TradeType: Optional[str] = None
    Trend: Optional[str] = None
    Spot_Price: Optional[float] = None
    Strike: Optional[float] = None
    Leg1_Strike: Optional[float] = None
    Leg1_Side: Optional[str] = None
    Leg1_Symbol: Optional[str] = None
    Leg1_Qty: Optional[int] = None
    Leg1_BuyPrice: Optional[float] = None
    Leg1_BuyOrderId: Optional[int] = None
    Leg1_SellPrice: Optional[float] = None
    Leg1_SellOrderId: Optional[int] = None
    Leg1_Sl_Price: Optional[float] = None
    Leg1_Sl_OrderId: Optional[int] = None
    Leg1_Tg_Price: Optional[float] = None
    Leg1_Tg_OrderId: Optional[int] = None
    Leg1_Pnl: Optional[float] = None
    Leg2_Strike: Optional[float] = None
    Leg2_Side: Optional[str] = None
    Leg2_Symbol: Optional[str] = None
    Leg2_Qty: Optional[int] = None
    Leg2_BuyPrice: Optional[float] = None
    Leg2_BuyOrderId: Optional[int] = None
    Leg2_SellPrice: Optional[float] = None
    Leg2_SellOrderId: Optional[int] = None
    Leg2_Sl_Price: Optional[float] = None
    Leg2_Sl_OrderId: Optional[int] = None
    Leg2_Tg_Price: Optional[float] = None
    Leg2_Tg_OrderId: Optional[int] = None
    Leg2_Pnl: Optional[float] = None
    Trade_StartTime: Optional[str] = None
    Trade_EndTime: Optional[str] = None
    Total_Premium: Optional[float] = None
    Total_Sl: Optional[float] = None
    LastPrice: Optional[float] = None
    LastPriceDate: Optional[str] = None
    MarketValue: Optional[float] = None
    Strategy: Optional[str] = None
    Instrument: Optional[str] = None
    Pyramid: Optional[int] = None
    UnderlyingSymbol: Optional[str] = None
    TradeDuration: Optional[str] = None
    SpreadNumber: Optional[int] = None
    SpreadType: Optional[str] = None
    SpreadStatus: Optional[str] = None
    Pnl: Optional[float] = None
    Charges: float
    PnlNet: Optional[float] = None
    Remarks: Optional[str] = None

    class Config:
        from_attributes = True


class HedgesSchemaIn(BaseModel):
    Broker: str
    UserId: str
    Date: Optional[str] = None
    Symbol: Optional[str] = None
    Status: Optional[str] = None
    ExpiryDate: Optional[str] = None
    ExpiryType: Optional[str] = None
    ProductType: Optional[str] = None
    Exchange: Optional[str] = None
    Segment: Optional[str] = None
    OptionType: Optional[str] = None
    Spot_Price: Optional[float] = None
    Strike: Optional[float] = None
    OrderSide: Optional[str] = None
    Quantity: Optional[int] = None
    BuyPrice: Optional[float] = None
    SellPrice: Optional[float] = None
    StopLossPrice: Optional[float] = None
    StopLossOrderID: Optional[float] = None
    TargetPrice: Optional[float] = None
    TargetOrderID: Optional[float] = None
    Trade_StartTime: Optional[str] = None
    Trade_EndTime: Optional[str] = None
    LastPrice: Optional[float] = None
    LastPriceDate: Optional[str] = None
    MarketValue: Optional[float] = None
    Strategy: Optional[str] = None
    Instrument: Optional[str] = None
    UnderlyingSymbol: Optional[str] = None
    Pnl: Optional[float] = None
    Charges: Optional[float] = None
    PnlNet: Optional[float] = None
    Remarks: Optional[str] = None

    class Config:
        from_attributes = True

class HedgesSchemaOut(BaseModel):
    HedgeId: int
    Broker: str
    UserId: str
    Date: Optional[str] = None
    Symbol: Optional[str] = None
    Status: Optional[str] = None
    ExpiryDate: Optional[str] = None
    ExpiryType: Optional[str] = None
    ProductType: Optional[str] = None
    Exchange: Optional[str] = None
    Segment: Optional[str] = None
    OptionType: Optional[str] = None
    Spot_Price: Optional[float] = None
    Strike: Optional[float] = None
    OrderSide: Optional[str] = None
    Quantity: Optional[int] = None
    BuyPrice: Optional[float] = None
    SellPrice: Optional[float] = None
    StopLossPrice: Optional[float] = None
    StopLossOrderID: Optional[float] = None
    TargetPrice: Optional[float] = None
    TargetOrderID: Optional[float] = None
    Trade_StartTime: Optional[str] = None
    Trade_EndTime: Optional[str] = None
    LastPrice: Optional[float] = None
    LastPriceDate: Optional[str] = None
    MarketValue: Optional[float] = None
    Strategy: Optional[str] = None
    Instrument: Optional[str] = None
    UnderlyingSymbol: Optional[str] = None
    Pnl: Optional[float] = None
    Charges: Optional[float] = None
    PnlNet: Optional[float] = None
    Remarks: Optional[str] = None

    class Config:
        from_attributes = True

class PLDateSummarySchema(BaseModel):
    Broker: str
    UserId: str
    Date: Optional[str] = None
    Strategy: Optional[str] = None
    Pnl: Optional[float] = None
    Charges: Optional[float] = None
    PnlNet: Optional[float] = None
    TradeType: Optional[str] = None
    Brokerage: Optional[float] = None
    Slippage: Optional[float] = None
    ActualPnl: Optional[float] = None
    ActualCharges: Optional[float] = None
    ActualPnlNet: Optional[float] = None
    ActualBrokerage: Optional[float] = None

    class Config:
        from_attributes = True


class PLFundsRiskSchema(BaseModel):
    Broker: str
    UserId: str
    DateTime: Optional[str] = None
    StartOfTheDayBalance: Optional[float] = None
    AvailableBalance: Optional[float] = None
    UtilizedBalance: Optional[float] = None
    UtilizationPercentage: Optional[float] = None
    UnrealizedProfit: Optional[float] = None
    RealizedProfit: Optional[float] = None
    PnlAmount: Optional[float] = None
    PnlPercentage: Optional[float] = None
    RiskAmount: Optional[float] = None
    RiskPercentage: Optional[float] = None

    class Config:
        from_attributes = True

class CreateOrderSchema(BaseModel):
    strategy: str
    exchange: str
    segment: str
    symbol: str
    productType: str
    orderType: str
    orderPurpose: str
    transactionType: str
    quantity: int
    orderPrice: float
    triggerPrice: float
    validity: str
    amo: str
    tag: str