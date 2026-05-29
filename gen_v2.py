#!/usr/bin/env python3
"""Generate the complete H5 Navigation Calculator in English, matching mini program 1.1.1."""
import os

OUT = r'D:\Users\Admin\Desktop\航海计算APP\index.html'

# ===================== CSS =====================
CSS = r"""*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f0f4f8;color:#333;max-width:750px;margin:0 auto;min-height:100vh}
.page-home{min-height:100vh;display:flex;flex-direction:column;background:linear-gradient(180deg,#e8edf5 0%,#f0f4f8 100%)}
.home-header{padding:30px 40px 20px;text-align:center}
.home-title{font-size:40px;font-weight:700;color:#004080}
.home-sub{font-size:16px;color:#666;margin-top:6px}
.menu-grid{padding:10px 16px;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.menu-item{background:#fff;border-radius:12px;padding:22px 16px;box-shadow:0 2px 12px rgba(0,0,0,.06);display:flex;flex-direction:column;align-items:center;text-align:center;cursor:pointer}
.menu-item:active{opacity:.8;transform:scale(.97)}
.menu-icon{width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:28px;margin-bottom:8px}
.icon-blue{background:#e3f0ff}.icon-cyan{background:#e0f7fa}.icon-teal{background:#e0f2f1}.icon-green{background:#e8f5e9}.icon-orange{background:#fff3e0}.icon-purple{background:#f3e5f5}.icon-brown{background:#efebe9}.icon-dark{background:#e8eaf0}
.menu-label{font-size:15px;font-weight:600;color:#333;margin-bottom:4px}
.menu-desc{font-size:11px;color:#888}
.tool-page{display:none;min-height:100vh;background:#f0f4f8;padding-bottom:60px}
.tool-page.active{display:block}
.back-bar{background:#fff;padding:12px 16px;position:sticky;top:0;z-index:100;box-shadow:0 1px 4px rgba(0,0,0,.06)}
.back-btn{display:flex;align-items:center;gap:6px;background:none;border:none;font-size:18px;color:#1F4E79;cursor:pointer;padding:4px 0}
.back-text{font-size:14px;font-weight:500}
.tool-header{text-align:center;padding:24px 16px 16px}
.header-icon{font-size:40px}
.header-title{display:block;font-size:24px;font-weight:700;color:#1F4E79;margin-top:4px}
.header-sub{display:block;font-size:13px;color:#8A9BB5;margin-top:4px}
.section{background:#fff;border-radius:12px;padding:16px;margin:0 12px 16px;box-shadow:0 2px 12px rgba(0,0,0,.06)}
.section-title{font-size:15px;font-weight:600;color:#1F4E79;margin-bottom:14px;padding-bottom:8px;border-bottom:2px solid #E8EDF3}
.input-section{border-left:4px solid #F5C518}
.result-section{border-left:4px solid #1F4E79}
.row{display:flex;gap:12px;margin-bottom:14px}
.row:last-child{margin-bottom:0}
.field{flex:1;min-width:0}
.field-label{display:block;font-size:13px;color:#444;margin-bottom:6px;font-weight:500}
.num-input{width:100%;min-height:42px;background:#F5F7FA;border:2px solid #DEE4EC;border-radius:5px;padding:8px 14px;font-size:16px;color:#333;outline:none}
.num-input:focus{border-color:#F5C518}
.num-input.yellow{border-color:#F0D080}
.num-input.yellow:focus{border-color:#F5C518}
.calc-btn{display:block;width:calc(100% - 24px);margin:0 12px 16px;padding:16px;background:linear-gradient(135deg,#004080,#1F4E79);color:#fff;border:none;border-radius:8px;font-size:18px;font-weight:700;cursor:pointer}
.calc-btn:active{opacity:.85;transform:scale(.98)}
.result-card{background:#F8FAFC;border-radius:8px;padding:14px;margin-top:6px}
.result-row{display:flex;justify-content:space-between;align-items:center;padding:6px 0}
.result-label{font-size:14px;color:#555}
.result-value{font-size:17px;font-weight:700;color:#004080}
.result-value.highlight{color:#D4A017;font-size:19px}
.result-value.warn{color:#C0392B}
.result-divider{height:1px;background:#E8EDF3;margin:2px 0}
.speed-table{width:100%;border-collapse:collapse;margin-top:8px;font-size:14px}
.speed-table td{padding:5px 8px;text-align:center;border-bottom:1px solid #E8EDF3}
.speed-table tr.highlight-row{background:#FFF8E1;font-weight:700}
.speed-table td:first-child{text-align:left;color:#888}
.footer{text-align:center;padding:20px;font-size:12px;color:#aaa}
.field-row{display:flex;align-items:center;gap:6px}
.ref-btn{width:32px;height:32px;border-radius:50%;background:#E8EDF3;display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer}
.auto-btn{background:#E3F0FF}
.cb-ref{background:#F8FAFC;border-radius:8px;padding:12px;margin-top:8px}
.cb-ref-title{font-size:13px;font-weight:600;color:#1F4E79;display:block;margin-bottom:8px}
.cb-ref-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px}
.cb-item{font-size:11px;color:#555;padding:2px}
.cb-calc-panel{background:#F0F7FF;border-radius:8px;padding:12px;margin-top:8px;border:1px solid #D0E0F0}
.cb-calc-title{font-size:13px;font-weight:600;color:#1F4E79;display:block;margin-bottom:8px}
.calc-cb-btn{display:block;width:100%;padding:10px;margin-top:10px;background:#1F4E79;color:#fff;border:none;border-radius:6px;font-size:14px;cursor:pointer}
.label-sm{font-size:12px;color:#555;display:block;margin-bottom:4px}
.note-text{display:block;font-size:12px;color:#888;margin-top:4px;line-height:1.5}
.result-grid{display:grid;gap:10px}
.result-grid.two{grid-template-columns:1fr 1fr}
.result-grid.three{grid-template-columns:1fr 1fr 1fr}
.result-item{background:#F8FAFC;border-radius:8px;padding:10px;text-align:center}
.r-label{font-size:11px;color:#888;display:block;margin-bottom:4px}
.r-value{font-size:20px;font-weight:700;color:#004080}
.r-value.new{color:#D4A017}
.r-value.warn{color:#C0392B}
.sep{height:1px;background:#E8EDF3;margin:8px 0}
.two-col{display:flex;gap:8px}
.col{flex:1}
.leg-row{margin-bottom:12px;padding:8px;background:#F8FAFC;border-radius:6px}
.leg-header{font-size:13px;font-weight:600;color:#1F4E79;margin-bottom:4px}
.leg-fromto{display:flex;align-items:center;gap:6px;margin-bottom:4px}
.legname{flex:1;min-height:36px;font-size:14px}
.leg-arrow{color:#888}
.leg-fields{display:flex;gap:4px;margin-bottom:2px}
.leg{flex:1;min-height:36px;font-size:13px;padding:4px 8px}
.leg-labels{display:flex;gap:4px}
.leg-labels span{flex:1;font-size:10px;color:#999;text-align:center}
.port-row{margin-bottom:12px;padding:8px;background:#F8FAFC;border-radius:6px}
.port-header{font-size:13px;font-weight:600;color:#1F4E79;margin-bottom:4px}
.portname{width:100%;min-height:36px;font-size:14px;margin-bottom:4px}
.port-fields{display:flex;gap:4px}
.port-fields input{flex:1;min-height:36px;font-size:13px;padding:4px 8px}
.compass-ref{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:6px;background:#F8FAFC;border-radius:8px;padding:8px}
.compass-ref div{text-align:center;font-size:12px;color:#666;padding:3px}
.compass-ref .dir-label{font-weight:600;color:#1F4E79;font-size:13px}
.orders-list{padding:0 12px}
.order-item{padding:12px 14px;background:#fff;margin-bottom:8px;border-radius:8px;font-size:14px;color:#333;border-left:3px solid #1F4E79}
.order-cat{font-size:11px;color:#8A9BB5;margin-bottom:4px}
.orders-header{display:flex;justify-content:space-between;align-items:center;padding:0 12px 12px}
.orders-date{font-size:13px;color:#8A9BB5}
.orders-actions{display:flex;gap:8px}
.orders-actions button{width:auto;margin:0}
.fuel-results{padding:8px}
.fuel-results table{width:100%;border-collapse:collapse;font-size:12px}
.fuel-results th,.fuel-results td{border:1px solid #DEE4EC;padding:4px 6px;text-align:center}
.fuel-results th{background:#1F4E79;color:#fff;font-size:11px}
.fuel-results td{background:#fff}
.status-banner{padding:10px 14px;border-radius:6px;font-weight:600;margin-bottom:12px;text-align:center;color:#fff}
@media(max-width:400px){.menu-grid{gap:8px;padding:8px}.menu-item{padding:16px 12px}.menu-label{font-size:13px}.menu-desc{font-size:10px}.header-title{font-size:20px}}
"""

print("CSS defined, length:", len(CSS))
