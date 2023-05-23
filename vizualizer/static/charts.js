import React, { useEffect, useRef } from 'react';

var chart = LightweightCharts.createChart(document.getElementById('charts'), {
	width: screen.width/1.25,
  	height: 500,
	layout: {
		backgroundColor: 'rgba(255,255,255,.5)',
		textColor: 'rgba(0, 0, 0, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	priceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
		timeVisible: true,
		secondsVisible: false,
	},
});

var candleSeries = chart.addCandlestickSeries({
	upColor: 'green',
	downColor: 'red', 
	borderDownColor: 'red',
	borderUpColor: 'green',
	wickDownColor: 'red',
	wickUpColor: 'green',
});

fetch('http://localhost:5000/history')
	.then((r) => r.json())
	.then((response) => {
		console.log(response)

		candleSeries.setData(response);
	})


var binanceSocket = new WebSocket("wss://stream.binance.us:9443/ws/ethusdt@kline_1m");

binanceSocket.onmessage = function (event) {	
	var message = JSON.parse(event.data);

	var candlestick = message.k;

	console.log(candlestick)

	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
}