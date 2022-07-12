from os import write
import streamlit as st
import pandas as pd
# import datetime as dt
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# import pickle
# import tensorflow as tf

# import datetime

st.set_page_config(
    page_title="Bitcoin Price Analysis",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# st.sidebar.title('Please select a page')
selected = st.sidebar.selectbox('Select a Page :', ['Data Visualization', 'Bitcoin Price Forecast'],index=0)
if selected == 'Data Visualization':
    st.markdown("<h1 style='text-align: center; color:  #34eb95; font-size: 42px ;'>Bitcoin Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    st.markdown("""<hr style="height:10x;border:none;color:#34eb95;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left; color:  cyan; font-size: 28px ;'>1. BTCUSDT 5 years Close Price Analysis</h1>", unsafe_allow_html=True)
    st.write()

    df = pd.read_csv('eda_btc.csv')
    df = df.set_index('date')
    # Price BTC chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index,
                    y=df['close'])) 
    fig.update_traces(line_color='Cyan', line_width=1)   # Set color for line chart

    # Add Cycle
    fig.add_vrect(x0="2017-08-17", x1="2020-11-01", y0=1, y1=0,
                annotation_text="Accumulation/sideways", annotation_position="top left", annotation_font_color="white",
                fillcolor="yellow", opacity=0.25, line_width=0)

    fig.add_vrect(x0="2020-11-5", x1="2021-11-09", 
                annotation_text="Uptrend", annotation_position="top left", annotation_font_color="white",
                fillcolor="green", opacity=0.25, line_width=0)

    fig.add_vrect(x0="2021-11-12", x1="2022-07-06", 
                annotation_text="Downtrend", annotation_position="top left", annotation_font_color="white",
                fillcolor="red", opacity=0.25, line_width=0)

    # Add line
    fig.add_hline(y=20000, annotation_text='2018 ALL TIME HIGH', annotation_position="top left", annotation_font_color="gold", opacity=0)
    fig.add_hline(y=67500, annotation_text='ALL TIME HIGH', annotation_position="bottom right", annotation_font_color="gold",opacity=0)
    fig.add_hline(y=4000, line_dash="dash", line_color="white", opacity=0.5)
    fig.add_hline(y=13000, line_dash="dash", line_color="white", opacity=0.5)

    # Labels
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Price")
    fig.update_yaxes(showline=False, linewidth=1, linecolor='black', gridcolor='black')

    # Background
    fig.update_layout(showlegend=False, legend_bgcolor='black')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    fig.update_layout(title_text='BTCUSDT Historical Price', title_x=0.5)
    fig.update_layout(autosize=True)

    # Drag mode
    fig.update_layout(dragmode='pan')
    fig.update_layout(template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

    st.expander('explanation', expanded=True)
    st.write("""From The Line Chart above we can see that, from the range of 2017 to 2022, there are three cycle of the BTCUSDT movement which are :
    \n\t
    1. accumulation/sideways 
    2. Uptrend
    3. Downtrend""")

    st.markdown('##### 1. Accumulation/sideways (Ranging from 4000 - 13000)')
    st.write("""At a glance, we can see that from july 2017 to jan 2021 the price moving sideways and ranging from around 4000 to 13000. However at the early of 2018, the BTC price reached 2018 ALL TIME HIGH at around 20000 before coming back to ranging price and stay at the sideways position for around 3.5 years.""")
    
    # Accumulation plot

    # Data
    accum = df['2017-08-17' :'2020-11-01']

    # Line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=accum.index,
                    y=accum['close'])) 
    fig.update_traces(line_color='Cyan', line_width=1)   # Set color for line chart

    # Add color and line
    fig.add_vrect(x0="2017-08-17", x1="2020-11-01", y0=1, y1=0,
                fillcolor="yellow", opacity=0.25, line_width=0)

    fig.add_hline(y=20000, annotation_text='2018 ALL TIME HIGH', annotation_position="top left", annotation_font_color="gold", opacity=0)
    fig.add_hline(y=8000, annotation_text='ACCUMULATION AREA', annotation_position="top left", annotation_font_color="white", opacity=0)
    fig.add_hrect(y0=12000, y1=13000, line_width=0, fillcolor="red", opacity=0.5)
    fig.add_hrect(y0=3000, y1=5000, line_width=0, fillcolor="green", opacity=0.5)

    # Layout setting
    fig.update_layout(title_text='Accumulation', title_x=0.5)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    fig.update_layout(width=800, height=400)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('##### 2. Uptrend Move (Creating higher high)')
    st.write("""Early November 2020, BTC has succeded to move above the resistance price (around 13000) and began to change from sideways to uptrend. This Uptrend move last for around 1 year and the BTC price was able to move from around 13000 to 67500 (ALL TIME HIGH) or increasing 419% from the start of that month to November 2021.""")
    
    # Uptrend plot
    # Data
    uptrend = df['2020-11-1' :'2021-11-13']

    # Line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=uptrend.index,
                    y=uptrend['close'])) 
    fig.update_traces(line_color='Cyan', line_width=1)   # Set color for line chart

    # Add color
    fig.add_vrect(x0="2020-11-5", x1="2021-11-09", 
                fillcolor="green", opacity=0.25, line_width=0)
    fig.add_hline(y=72000, annotation_text='ALL TIME HIGH', annotation_position="bottom right", annotation_font_color="gold",opacity=0)

    # Layout setting
    fig.update_layout(title_text='Uptrend Move', title_x=0.5)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    fig.update_layout(width=800, height=400)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('##### 3. Downtrend Move (Creating lower low)')
    st.write("""Toward the end of November 2021 to current date, The price began to move lower and lower decreasing from ALL TIME HIGH price at 67500 to around 20000 (currently) or losing value 70% since all time high.""")
    
    # Downtrend plot
    downtrend = df['2021-11-01' :'2022-07-10']

    # Line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=downtrend.index,
                    y=downtrend['close'])) 
    fig.update_traces(line_color='Cyan', line_width=1)   # Set color for line chart

    # Add color
    fig.add_vrect(x0="2021-11-12", x1="2022-07-06", 
                fillcolor="red", opacity=0.25, line_width=0)

    # Layout setting
    fig.update_layout(title_text='Downtrend Move', title_x=0.5)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    fig.update_layout(width=800, height=400)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<h1 style='text-align: left; color:  cyan; font-size: 28px ;'>2. BTCUSDT Support and Resistance</h1>", unsafe_allow_html=True)
    st.write()
    st.markdown('##### What is support and resistance ?')
    st.write("""According to investopedia, Support is a price level where a downtrend can be expected to pause due to a concentration of demand or buying interest. As the price of assets or securities drops, demand for the shares increases, thus forming the support line. Meanwhile, resistance zones arise due to selling interest when prices have increased.""")
    st.markdown('##### How do we use support and resistance ?')
    st.write("""Once we indentified the support and the resistance area, we will be able to know where the price will be possibly be stopped or halted its move. Hence, we can use that area as an entry and exit point. However, we have to be always trade and use those area carefully since once the price reaching support and resistance area, the price will do two things which are reverse its direction or continuing its initial direction.
    \n
    source : https://www.investopedia.com/trading/support-and-resistance-basics/""")

    st.write('Plotting Support and Resistance area for BTCUSD :')
    # Price BTC chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index,
                    y=df['close'])) 
    fig.update_traces(line_color='Cyan', line_width=1)   # Set color for line chart

    # ADD horizontal line
    fig.add_hline(y=30000 , line_color="yellow", opacity = 0.5)
    fig.add_hline(y=20000, line_dash="dash", line_color="limegreen")
    fig.add_hline(y=13000, line_dash="dash", line_color="limegreen")
    fig.add_hrect(y0=13000, y1=20000, line_width=0, fillcolor="green", opacity=0.2, annotation_text='SUPPORT', annotation_position="top left")

    fig.add_hline(y=63500, line_dash="dash", line_color="tomato")
    fig.add_hline(y=67500, line_dash="dash", line_color="tomato")
    fig.add_hrect(y0=63500, y1=67500, line_width=0, fillcolor="red", opacity=0.2, annotation_text='RESISTANCE', annotation_position="top left")

    # Labels
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Price")
    fig.update_yaxes(showline=False, linewidth=1, linecolor='black', gridcolor='black')

    # Background
    fig.update_layout(showlegend=False, legend_bgcolor='black')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    fig.update_layout(title_text='Support and Resistance', title_x=0.5)
    fig.update_layout(autosize=True)

    # Drag mode
    fig.update_layout(dragmode='pan')
    fig.update_layout(template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

    st.expander('explanation', expanded=True)
    st.write("""Taking a look at the given chart, we can see that there three key areas for the BTCUSDT, which are :
    \n
    1. Resistance area, an area where the price normally stops rising and dips back down.
    2. Support area, an area where the price regularly stops falling and bounces back up.
    3. yellow line, the yellow line here acted as the previous support which was just recently broken down, so now this line will serve as current resistance.""")
    st.write("""The current situation with BTC :
    \n
    As we can see from the chart above, the BTCUSDT price currently being halted at a support area at around 20000. what we can expect from this is :

    1. if the price stops falling and begin to bounces back up and even break above yellow line (30000), then this the area above 20000 and 30000 will be a good time to entry.
    2. if the price break down below support area (below 13000), then this will mean that the price will continue to go down until the price reach the next support at around 3000 to 5000.
    """)

    st.markdown("<h1 style='text-align: left; color:  cyan; font-size: 28px ;'>3. Volume Analysis</h1>", unsafe_allow_html=True)
    st.write()

    # Creating new dataset for volume analysis
    df_volume = df.copy()
    df_volume['diff'] = df_volume['close'] - df_volume['open']
    df_volume.loc[df_volume['diff']>=0, 'color'] = 'green'
    df_volume.loc[df_volume['diff']<0, 'color'] = 'red'
    df_volume['volbtc_MA_20'] = df_volume['Volume BTC'].rolling(20).mean()
    df_volume['volusdt_MA_20'] = df_volume['Volume USDT'].rolling(20).mean()

    st.write('Plotting the Volume BTC and Volume USDT :')
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=('Volume BTC', 'Volume USDT'), row_width=[0.3,0.3])

    fig.add_trace(go.Bar(x=df.index, y=df['Volume BTC'], showlegend=False, opacity = 1, marker={'color': 'white'}), row=1, col=1)
    fig.add_trace(go.Bar(x=df.index, y=df['Volume USDT'], showlegend=False, opacity = 1, marker={'color': 'cyan'}), row=2, col=1)

    vol_btc = go.Scatter(x=df_volume.index, y=df_volume['volbtc_MA_20'], mode='lines', name='ma 20', showlegend=False)
    fig.add_trace(vol_btc, row=1, col=1)

    vol_usdt = go.Scatter(x=df_volume.index, y=df_volume['volusdt_MA_20'], mode='lines', name='ma 20', showlegend=False)
    fig.add_trace(vol_usdt, row=2, col=1)

    # Add Cycle
    fig.add_vrect(x0="2017-08-17", x1="2020-11-01", y0=1, y1=0,
                annotation_text="Accumulation/sideways", annotation_position="top left", annotation_font_color="white",
                fillcolor="yellow", opacity=0.2, line_width=0)

    fig.add_vrect(x0="2020-11-5", x1="2021-11-09", 
                annotation_text="Uptrend", annotation_position="top left", annotation_font_color="white",
                fillcolor="green", opacity=0.2, line_width=0)

    fig.add_vrect(x0="2021-11-12", x1="2022-07-06", 
                annotation_text="Downtrend", annotation_position="top left", annotation_font_color="white",
                fillcolor="red", opacity=0.2, line_width=0)

    fig.update_layout(
        # title = 'JKSE historical price',
        xaxis_tickfont_size = 12,
        xaxis2 = dict(
            title = 'Date',
            titlefont_size=14,
            tickfont_size=12
        ),
        autosize=True,
    )

    fig.update_yaxes(title_text="Volume")

    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    st.plotly_chart(fig, use_container_width=True)

    st.expander('explanation', expanded=True)
    st.write("""For the Volume BTC,
    \n
    1. accumulation : during accumulation, the volume was stagnant at the beginning and began to increase at the end of accumulation process.
    2. Uptrend : the volume was at the highest during the Uptrend meaning that the uptrend move was validated. However, it began to decrease toward the end of the uptrend move which might means than the uptrend move is almost ended.
    3. Downtrend : during downtrend, the volume was low at the beginning and slowly getting higher. This might mean that as the price is currently reached the support area, some trader might consider that this is the best price to entry.""")
    st.write("""For Volume USDT,
    \n
    1. Accumulation : the volume was the lowest
    2. Uptrend : the volume was the highest during the uptrend move, it seems that as the volume BTC traded higher after the breakout from sideways move, the volume USDT also followed suit.
    3. Downtrend : Volume USDT began to decrese during the downtrend.
    """)

    st.markdown("<h1 style='text-align: left; color:  cyan; font-size: 28px ;'>4. BTCUSDT Performance</h1>", unsafe_allow_html=True)
    st.write()

    st.markdown("<h1 style='text-align: left; color:  yellow; font-size: 20px ;'>7-days Performance :</h1>", unsafe_allow_html=True)
    # Create dataframe for 7 days data
    seven_day = df_volume['2022-06-30' :'2022-07-06']

    # Plot 7-Days Candlestick
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=('BTCUSDT', 'Volume'), row_width=[0.3,0.8])

    fig.add_trace(go.Candlestick(x=seven_day.index,
                    open=seven_day['open'],
                    high=seven_day['high'],
                    low=seven_day['low'],
                    close=seven_day['close'], name = 'Price', showlegend=False), row=1, col=1)

    fig.add_trace(go.Bar(x=seven_day.index, y=seven_day['Volume BTC'], showlegend=False, opacity = 1, marker={'color': df_volume['color']}), row=2, col=1)

    fig.update_layout(
        # title = 'JKSE historical price',
        xaxis_tickfont_size = 12,
        yaxis = dict(
            title = 'Price',
            titlefont_size=14,
            tickfont_size=12
        ),
        autosize=True,
    )

    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    st.plotly_chart(fig, use_container_width=True)

    st.write('7-DAYs PERFORMANCE :', round((seven_day['close'][-1]-seven_day['open'][0])*100/seven_day['open'][0],2),'%')
    st.write('Average Volume', round(sum(seven_day['Volume BTC']),2))
    st.write('Looking at the performance of BTCUSDT using recent 7-days data, we can see that the price movement can be considered stagnant and moving sideways since from 7-days candlestick, the price only move +0.45 %.')
    st.write()

    st.markdown("<h1 style='text-align: left; color:  yellow; font-size: 20px ;'>30-Days Performance :</h1>", unsafe_allow_html=True)
    # Create dataframe for 7 days data
    monthly = df_volume['2022-06-07' :'2022-07-06']
    # Plot 30-Days Candlestick
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=('BTCUSDT', 'Volume'), row_width=[0.3,0.8])

    fig.add_trace(go.Candlestick(x=monthly.index,
                    open=monthly['open'],
                    high=monthly['high'],
                    low=monthly['low'],
                    close=monthly['close'], name = 'Price', showlegend=False), row=1, col=1)

    fig.add_trace(go.Bar(x=monthly.index, y=monthly['Volume BTC'], showlegend=False, opacity = 1, marker={'color': monthly['color']}), row=2, col=1)

    fig.update_layout(
        # title = 'JKSE historical price',
        xaxis_tickfont_size = 12,
        yaxis = dict(
            title = 'Price',
            titlefont_size=14,
            tickfont_size=12
        ),
        autosize=True,
    )


    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    st.plotly_chart(fig, use_container_width=True)

    st.write('30-DAYs PERFORMANCE :', round((monthly['close'][29]-monthly['open'][0])*100/monthly['open'][0],2),'%')
    st.write('Average Volume', round(sum(monthly['Volume BTC']),2))
    st.write('From 30-Days Performance, BTCUSD was moving downtrend since the price was down for -35.57% and the average of Volume was 2.864.816,49')
    st.write()

    st.markdown("<h1 style='text-align: left; color:  yellow; font-size: 20px ;'>YTD Performance :</h1>", unsafe_allow_html=True)
    # Create dataframe for 7 days data
    ytd = df_volume['2022-01-01' :'2022-07-06']
    # Plot YTD Candlestick
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=('BTCUSDT', 'Volume'), row_width=[0.3,0.8])

    fig.add_trace(go.Candlestick(x=ytd.index,
                    open=ytd['open'],
                    high=ytd['high'],
                    low=ytd['low'],
                    close=ytd['close'], name = 'Price', showlegend=False), row=1, col=1)

    fig.add_trace(go.Bar(x=ytd.index, y=ytd['Volume BTC'], showlegend=False, opacity = 1, marker={'color': ytd['color']}), row=2, col=1)

    fig.update_layout(
        # title = 'JKSE historical price',
        xaxis_tickfont_size = 12,
        yaxis = dict(
            title = 'Price',
            titlefont_size=14,
            tickfont_size=12
        ),
        autosize=True,
    )


    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    st.plotly_chart(fig, use_container_width=True)

    st.write('YTD-DAYs PERFORMANCE :', round((ytd['close'][-1]-ytd['open'][0])*100/ytd['open'][0],2),'%')
    st.write('Average Volume', round(sum(ytd['Volume BTC']),2))
    st.write('Since the beginning of the year, the BTC has been moving downtrend. The price has been decreasing for -56.26 % and the average trading volume was 10.886.531,37')
    st.write()

    st.markdown("<h1 style='text-align: left; color:  cyan; font-size: 28px ;'>5. Technical analysis with Moving Averages</h1>", unsafe_allow_html=True)
    st.write()
    
    st.markdown('##### What is Moving averages ?')
    st.write("""According to CFI team, A moving average is a technical indicator that market analysts and investors may use to determine the direction of a trend. It sums up the data points of a financial security over a specific time period and divides the total by the number of data points to arrive at an average. Furthermore, a moving average also can be used to determine support and resistance. Hence, a moving average helps to indentify when to enter and exit from the market.""")

    # Moving average
    df_volume['MA_20'] = df_volume['close'].rolling(window=20, min_periods=0).mean()
    df_volume['MA_50'] = df_volume['close'].rolling(window=50, min_periods=0).mean()
    df_volume['MA_200'] = df_volume['close'].rolling(window=200, min_periods=0).mean()

    # MACD : 12 day EMA - 26-day ema
    df_volume['26_ema'] = df_volume['close'].ewm(span=26,min_periods=0,adjust=True,ignore_na=False).mean()
    df_volume['12_ema'] = df_volume['close'].ewm(span=12,min_periods=0,adjust=True,ignore_na=False).mean()
    df_volume['MACD'] = df_volume['12_ema'] - df_volume['26_ema']
    df_volume['signal'] = df_volume['MACD'].ewm(span=9,min_periods=0,adjust=True,ignore_na=False).mean()

    # slice to 200 days
    df_volume = df_volume[-200:]
    # Plot the chart with technical indicators

    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05, subplot_titles=('BTCUSDT', 'Volume', 'MACD'), row_width=[0.3,0.2,1])

    fig.add_trace(go.Candlestick(x=df_volume.index,
                    open=df_volume['open'],
                    high=df_volume['high'],
                    low=df_volume['low'],
                    close=df_volume['close'], name = 'Price',increasing_line_color= 'lightseagreen', decreasing_line_color= 'tomato'), row=1, col=1)

    fig.add_trace(go.Scatter(x=df_volume.index, y=df_volume['MA_20'], marker_color='green', name='MA20', opacity=0.5), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_volume.index, y=df_volume['MA_50'], marker_color='yellow', name='MA50', opacity=0.5), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_volume.index, y=df_volume['MA_200'], marker_color='red', name='MA200', opacity=0.5), row=1, col=1)
    fig.add_trace(go.Bar(x=df_volume.index, y=df_volume['Volume BTC'], showlegend=False, marker={'color':df_volume['color']}), row=2, col=1)
    vol_btc = go.Scatter(x=df_volume.index, y=df_volume['volbtc_MA_20'], mode='lines', marker_color= 'yellow', name='ma 20', showlegend=False)
    fig.add_trace(vol_btc, row=2, col=1)


    # plot MACD
    fig.add_trace(go.Scatter(x=df_volume.index,
                            y=df_volume['MACD'], name='MACD', showlegend=False), row=3, col=1) 
    fig.add_trace(go.Scatter(x=df_volume.index,
                            y=df_volume['signal'], name = 'Signal', showlegend=False), row=3, col=1) 
    fig.add_hline(y=0 , line_color="red", opacity = 0.5, row=3, col=1)

    fig.update_layout(
        xaxis_tickfont_size = 12,
        yaxis = dict(
            title = 'Price',
            titlefont_size=14,
            tickfont_size=12
        ),
        autosize=False,
        width=1000,
        height=800,
        # paper_bgcolor = 'Black'
    )

    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(dragmode='pan')
    fig.update_layout(showlegend=False)
    fig.update_layout(paper_bgcolor='black',plot_bgcolor='black', font_color = 'white')
    st.plotly_chart(fig, use_container_width=True)

    st.expander('explanation', expanded=True)
    st.write("""
    \n
    1. In this analysis, 20-days MA can be used to define short-term trend. For Example if the price move above these 20-days MA, then from short-term perspective the trend is bullish. On the other hand, if the price move below 20-days MA, we can see it as short-term bearish.
    2. 50-days moving average can be used to see whether the index is bullish or bearish from the medium-term perspective. Above 50-days moving average the trend is bullish while below 50 days MA is bearish.
    3. 200-days MA to define longer preiod market trend. Above 100 MA or 200-days MA from long-term perspective can be cactegorize as bullish while if the opposite it is bearish. """)

    st.markdown("<h1 style='text-align: left; color:  yellow; font-size: 20px ;'>So, what is the current situation on BTCUSDT if we see it from technical perpesctive using moving averages as indicators?</h1>", unsafe_allow_html=True)
    st.markdown(""" From technical perspective:
    \n
    The current price for BTCUSDT price is below its 20-days, 50-days, and 200-days MA. This is an indication that the price is in downtrend movement since it can be seen that from short-term, medium-term, and long-term all indicate that the current price for BTCUSDT is in bearish periods. 

    The Moving average usually used by trader and investor as dynamic support and resistance and can be used to time when to entry an exit the market. For Example, for BTSUDT chart above, if the price move above 20-days MA (indicating short-term bullish), then we can used it as a timing to enter the market or buy BTC. Here, the 20-days MA will act as its dynamic support so once the price move below 20-days MA, the trader should exit the market since it broke down below the support area or 20-days MA.""")


elif selected == 'Bitcoin Price Forecast':
    st.markdown("<h1 style='text-align: center; color:  #34eb95; font-size: 42px ;'>Bitcoin Price Forecast</h1>", unsafe_allow_html=True)
    st.markdown("""<hr style="height:10x;border:none;color:#34eb95;background-color:#333;" /> """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)
    with col1:
        selected_stock = st.text_input("Enter a valid cryptocurrency ticker...", "BTC-USD")
    with col2:
        periods = st.selectbox(label = 'Select the periods :', options=('1d','5d','1mo','3mo','6mo','1y','5y','ytd','max'), index=7)
    with col3:
        legend=st.selectbox(label = 'Show legend', options=(True,False), index=0)

    # Chart
    get_data = yf.Ticker(selected_stock)
    df = pd.DataFrame(get_data.history(period=periods), columns=['Open','High', 'Low', 'Close', 'Volume'])
    df['MA20'] = df['Close'].rolling(window=20, min_periods=0).mean()
    df['MA50'] = df['Close'].rolling(window=50, min_periods=0).mean()
    df['MA200'] = df['Close'].rolling(window=200, min_periods=0).mean()
    df['diff'] = df['Close'] - df['Open']
    df.loc[df['diff']>=0, 'color'] = 'lightseagreen'
    df.loc[df['diff']<0, 'color'] = 'tomato'
    df['volbtc_MA_20'] = df['Volume'].rolling(20).mean()

    # MACD : 12 day EMA - 26-day ema
    df['26_ema'] = df['Close'].ewm(span=26,min_periods=0,adjust=True,ignore_na=False).mean()
    df['12_ema'] = df['Close'].ewm(span=12,min_periods=0,adjust=True,ignore_na=False).mean()
    df['MACD'] = df['12_ema'] - df['26_ema']
    df['signal'] = df['MACD'].ewm(span=9,min_periods=0,adjust=True,ignore_na=False).mean()


    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05, subplot_titles=(f'{selected_stock}', 'Volume', 'MACD'), row_width=[0.3,0.2,1])

    fig.add_trace(go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'], name = 'Price',increasing_line_color= 'lightseagreen', decreasing_line_color= 'tomato'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['MA20'], marker_color='green', name='MA20', opacity=0.5), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['MA50'], marker_color='yellow', name='MA50', opacity=0.5), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['MA200'], marker_color='red', name='MA200', opacity=0.5), row=1, col=1)
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], showlegend=False, marker={'color':df['color']}), row=2, col=1)
    vol_btc = go.Scatter(x=df.index, y=df['volbtc_MA_20'], mode='lines', name='ma 20', showlegend=False)
    fig.add_trace(vol_btc, row=2, col=1)


    # plot MACD
    fig.add_trace(go.Scatter(x=df.index,
                            y=df['MACD'], name='MACD', showlegend=False), row=3, col=1) 
    fig.add_trace(go.Scatter(x=df.index,
                            y=df['signal'], name = 'Signal', showlegend=False), row=3, col=1) 

    fig.update_layout(
        xaxis_tickfont_size = 12,
        yaxis = dict(
            title = 'Price',
            titlefont_size=14,
            tickfont_size=12
        ),
        autosize=False,
        width=800,
        height=800,
        # margin=dict(l=50, r=50, b=100, t=100, pad=5),
        paper_bgcolor = 'Black'
    )
    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(template='plotly_dark')
    fig.update_layout(dragmode='pan')
    fig.update_layout(showlegend=legend)
    st.plotly_chart(fig, use_container_width=True)

    # prediction
    
    # with open("prep_pipeline.pkl", "rb") as f:
    #     pickled_model = pickle.load(f)
    # # pickled_model = pickle.load(open('prep_pipeline.pkl', 'rb'))
    # saved_model = tf.keras.models.load_model('model_best.hdf5')

    # data0 = yf.Ticker(selected_stock)
    # data_inference = pd.DataFrame(data0.history(period="30d"), columns=['Close'])

    # data_inf = pickled_model.transform(data_inference)
    # X_next = data_inf.reshape(1, 30, 1)
    # next_day = saved_model.predict(X_next)
    # next_day = pickled_model.inverse_transform(next_day)
    # next_day

    st.markdown("<h1 style='text-align: center; color:  #34eb95; font-size: 20px ;'>Next Day price prediction is :</h1>", unsafe_allow_html=True)
    st.expander('see explanation',expanded=False)
    st.write('SORRY!!! Model deployment is under maintenance')