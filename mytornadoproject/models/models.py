# coding: utf-8
from sqlalchemy import Column, DECIMAL, Float, ForeignKey, LargeBinary, String, Text
from sqlalchemy.dialects.mysql import DATETIME, INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BarraFactorWeek(Base):
    __tablename__ = 'barra_factor_week'

    date = Column(String(12), primary_key=True, nullable=False)
    stock_code = Column(String(20), primary_key=True, nullable=False)
    Pb = Column(DECIMAL(20, 8))
    Turn = Column(DECIMAL(20, 8))
    Mkt = Column(DECIMAL(20, 8))
    Close = Column(DECIMAL(20, 8))
    Roe = Column(DECIMAL(20, 8))
    Yoyroe = Column(DECIMAL(20, 8))
    Debttoassets = Column(DECIMAL(20, 8))
    IndexComponent = Column(DECIMAL(20, 8))


class DjangoMigration(Base):
    __tablename__ = 'django_migrations'

    id = Column(INTEGER(11), primary_key=True)
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DATETIME(fsp=6), nullable=False)


class FundIndex(Base):
    __tablename__ = 'fund_index'

    FI_id = Column(INTEGER(10), primary_key=True)
    index_name = Column(String(50))
    index_code = Column(String(50))
    income_rate = Column(Float(20))
    max_retreat_rate = Column(Float(20))
    sharpe_ratio = Column(Float(20))


class FundProduct(Base):
    __tablename__ = 'fund_products'

    FP_id = Column(INTEGER(10), primary_key=True)
    products_name = Column(String(50), nullable=False)
    investment_advisor = Column(String(50), nullable=False)
    income = Column(String(50), nullable=False)
    risk = Column(String(100), nullable=False)
    product_type = Column(String(50), nullable=False)
    net_disclosure_frequency = Column(String(50), nullable=False)
    style_evaluation = Column(String(70), nullable=False)
    result_type = Column(String(50), nullable=False)
    value = Column(Text, nullable=False)


class FundRecommendation(Base):
    __tablename__ = 'fund_recommendation'

    FR_id = Column(INTEGER(10), primary_key=True)
    fund_type = Column(String(20), nullable=False)
    sorte = Column(String(20), nullable=False)
    value = Column(Text, nullable=False)


class FundType(Base):
    __tablename__ = 'fund_type'

    Type_id = Column(INTEGER(10), primary_key=True)
    Level_one = Column(String(50))
    Level_two = Column(String(50))
    Level_three = Column(String(50))
    Level_four = Column(String(50))
    Level_fives = Column(String(50))
    Level_six = Column(String(50))
    Level_seven = Column(String(50))
    Level_eight = Column(String(50))


class IndexCloseDay(Base):
    __tablename__ = 'index_close_day'

    date = Column(String(20), primary_key=True)
    _000011_SH = Column('000011.SH', DECIMAL(20, 8))
    _000012_SH = Column('000012.SH', DECIMAL(20, 8))
    _000300_SH = Column('000300.SH', DECIMAL(20, 8))
    _000985_CSI = Column('000985.CSI', DECIMAL(20, 8))
    _881001_WI = Column('881001.WI', DECIMAL(20, 8))
    NH0100_NHF = Column('NH0100.NHF', DECIMAL(20, 8))
    _885008_WI = Column('885008.WI', DECIMAL(20, 8))
    H11023_CSI = Column('H11023.CSI', DECIMAL(20, 8))
    _399372_SZ = Column('399372.SZ', DECIMAL(20, 8))
    _399373_SZ = Column('399373.SZ', DECIMAL(20, 8))
    _399374_SZ = Column('399374.SZ', DECIMAL(20, 8))
    _399375_SZ = Column('399375.SZ', DECIMAL(20, 8))
    _399376_SZ = Column('399376.SZ', DECIMAL(20, 8))
    _399377_SZ = Column('399377.SZ', DECIMAL(20, 8))
    _801010_SI = Column('801010.SI', DECIMAL(20, 8))
    _801020_SI = Column('801020.SI', DECIMAL(20, 8))
    _801030_SI = Column('801030.SI', DECIMAL(20, 8))
    _801040_SI = Column('801040.SI', DECIMAL(20, 8))
    _801050_SI = Column('801050.SI', DECIMAL(20, 8))
    _801080_SI = Column('801080.SI', DECIMAL(20, 8))
    _801110_SI = Column('801110.SI', DECIMAL(20, 8))
    _801120_SI = Column('801120.SI', DECIMAL(20, 8))
    _801130_SI = Column('801130.SI', DECIMAL(20, 8))
    _801140_SI = Column('801140.SI', DECIMAL(20, 8))
    _801150_SI = Column('801150.SI', DECIMAL(20, 8))
    _801160_SI = Column('801160.SI', DECIMAL(20, 8))
    _801170_SI = Column('801170.SI', DECIMAL(20, 8))
    _801180_SI = Column('801180.SI', DECIMAL(20, 8))
    _801200_SI = Column('801200.SI', DECIMAL(20, 8))
    _801210_SI = Column('801210.SI', DECIMAL(20, 8))
    _801230_SI = Column('801230.SI', DECIMAL(20, 8))
    _801710_SI = Column('801710.SI', DECIMAL(20, 8))
    _801720_SI = Column('801720.SI', DECIMAL(20, 8))
    _801730_SI = Column('801730.SI', DECIMAL(20, 8))
    _801740_SI = Column('801740.SI', DECIMAL(20, 8))
    _801750_SI = Column('801750.SI', DECIMAL(20, 8))
    _801760_SI = Column('801760.SI', DECIMAL(20, 8))
    _801770_SI = Column('801770.SI', DECIMAL(20, 8))
    _801780_SI = Column('801780.SI', DECIMAL(20, 8))
    _801790_SI = Column('801790.SI', DECIMAL(20, 8))
    _801880_SI = Column('801880.SI', DECIMAL(20, 8))
    _801890_SI = Column('801890.SI', DECIMAL(20, 8))
    _885005_WI = Column('885005.WI', DECIMAL(20, 8))
    _885010_WI = Column('885010.WI', DECIMAL(20, 8))
    _885011_WI = Column('885011.WI', DECIMAL(20, 8))
    _885012_WI = Column('885012.WI', DECIMAL(20, 8))
    _885013_WI = Column('885013.WI', DECIMAL(20, 8))
    TB10Y_WI = Column('TB10Y.WI', DECIMAL(20, 8))
    SHIBORON_IR = Column('SHIBORON.IR', DECIMAL(20, 8))
    _000903_SH = Column('000903.SH', DECIMAL(20, 8))
    _000852_SH = Column('000852.SH', DECIMAL(20, 8))


class MarketStrategy(Base):
    __tablename__ = 'market_strategy'

    MS_id = Column(INTEGER(10), primary_key=True)
    strategyNamelist = Column(String(100), nullable=False)
    startTime = Column(String(50), nullable=False)
    benchmarkName = Column(String(50), nullable=False)
    name = Column(String(50))
    output_description = Column(String(50))
    value = Column(Text)


class PersonalTable(Base):
    __tablename__ = 'personal_table'

    User_ID = Column(INTEGER(10), primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    phone = Column(INTEGER(15))
    idcard = Column(String(20))
    name = Column(String(20))
    collent = Column(String(1000))
    history = Column(String(1000))


class ProductPerformance(Base):
    __tablename__ = 'product_performance'

    PP_id = Column(INTEGER(10), primary_key=True)
    timeRange = Column(String(50), nullable=False)
    bench_name = Column(String(50))
    fund_code = Column(String(50))
    datetype = Column(String(4), nullable=False)
    fund_type = Column(String(50))
    name = Column(String(50))
    output_description = Column(String(50))
    value = Column(Text)


class ProductRanking(Base):
    __tablename__ = 'product_ranking'

    PR_id = Column(INTEGER(10), primary_key=True)
    type = Column(String(20), nullable=False)
    date = Column(String(20), nullable=False)
    value = Column(Text, nullable=False)


class RecommendedSelection(Base):
    __tablename__ = 'recommended_selection'

    RS_id = Column(INTEGER(10), primary_key=True)
    fund_name = Column(String(50))
    fund_code = Column(String(50))
    income_rate = Column(Float(20))
    max_retreat_rate = Column(Float(20))


class SceneAnalysi(Base):
    __tablename__ = 'scene_analysis'

    SA_id = Column(INTEGER(10), primary_key=True)
    bench_name = Column(String(50), nullable=False)
    fund_code = Column(String(50), nullable=False)
    rf = Column(Float(50), nullable=False)
    market_type = Column(String(50))
    special_fund_type = Column(String(50))
    scenario = Column(String(50))
    analytical_method = Column(String(50))
    name = Column(String(50))
    output_description = Column(String(50))
    value = Column(Text)


class ScoringSystem(Base):
    __tablename__ = 'scoring_system'

    SM_id = Column(INTEGER(10), primary_key=True)
    begin_time = Column(String(50), nullable=False)
    temp_date = Column(String(50), nullable=False)
    viewing_time = Column(String(50), nullable=False)
    end_time = Column(String(50), nullable=False)
    name = Column(String(50))
    output_description = Column(String(50))
    value = Column(LargeBinary)


class StyleAttribution(Base):
    __tablename__ = 'style_attribution'

    ST_id = Column(INTEGER(10), primary_key=True)
    netvalue_type = Column(String(4), nullable=False)
    fund_name = Column(String(50), nullable=False)
    bench_name = Column(String(50), nullable=False)
    pure_ele_type = Column(String(4), nullable=False)
    name = Column(String(50))
    output_description = Column(String(50))
    value = Column(LargeBinary)


class FundCoverageDay(Base):
    __tablename__ = 'fund_coverage_day'

    Type_id = Column(ForeignKey(u'fund_type.Type_id'), primary_key=True, nullable=False)
    fund_code = Column(String(20), primary_key=True, nullable=False)
    nav_date = Column(String(20))
    netasset_total = Column(DECIMAL(20, 8))
    purchase_redempti = Column(String(20))
    product_performance_label = Column(INTEGER(2))
    product_rating_label = Column(INTEGER(2))

    Type = relationship(u'FundType')


class FundList(Base):
    __tablename__ = 'fund_list'

    Type_id = Column(ForeignKey(u'fund_type.Type_id'), primary_key=True, nullable=False)
    fund_code = Column(String(20), primary_key=True, nullable=False)
    fund_setupdate = Column(String(20))
    fund_maturitydate = Column(String(20))
    nav_updatefrequency = Column(String(4))
    fund_type = Column(String(20))
    fund_firstinvesttype = Column(String(20))
    fund_investtype = Column(String(20))
    fund_structuredfundornot = Column(String(2))
    fund_parvalue = Column(DECIMAL(20, 8))
    fund_fullname = Column(String(30))
    curr = Column(String(8))
    fund_manager = Column(String(30))

    Type = relationship(u'FundType')


class FundUpdateDay(Base):
    __tablename__ = 'fund_update_day'

    Type_id = Column(ForeignKey(u'fund_type.Type_id'), primary_key=True, nullable=False)
    fund_code = Column(String(20), primary_key=True, nullable=False)
    date = Column(String(12), primary_key=True, nullable=False)
    nav_adj = Column(DECIMAL(20, 8))

    Type = relationship(u'FundType')


class ScoreDateMonth(Base):
    __tablename__ = 'score_date_month'

    Type_id = Column(ForeignKey(u'fund_type.Type_id'), primary_key=True, nullable=False)
    date = Column(String(20), primary_key=True, nullable=False)
    fund_name = Column(DECIMAL(20, 8), primary_key=True, nullable=False)
    risk_nonsysrisk23 = Column(DECIMAL(20, 8))
    risk_calmar = Column(DECIMAL(20, 8))
    risk_beta = Column(DECIMAL(20, 8))
    risk_treynor12 = Column(DECIMAL(20, 8))
    risk_treynor23 = Column(DECIMAL(20, 8))
    risk_jensen = Column(DECIMAL(20, 8))
    risk_sortino = Column(DECIMAL(20, 8))
    risk_time = Column(DECIMAL(20, 8))
    risk_nonsysrisk05 = Column(DECIMAL(20, 8))
    risk_stock = Column(DECIMAL(20, 8))
    Half_year_fund_returns = Column('Half-year_fund_returns', DECIMAL(20, 8))
    Half_year_Baseline__income300 = Column('Half-year_Baseline_ income300', DECIMAL(20, 8))
    Half_year_Baseline__income905 = Column('Half-year_Baseline_ income905', DECIMAL(20, 8))

    Type = relationship(u'FundType')
