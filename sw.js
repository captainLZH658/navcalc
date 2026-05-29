const CACHE_NAME = 'pwa-cache-v1';
const OFFLINE_URL = '/offline.html';

const PRECACHE = ['/','/offline.html','/manifest.json','/icons/icon-192x192.png','/icons/icon-512x512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(PRECACHE)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))));
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (['image','style','script','font'].includes(e.request.destination)) {
    e.respondWith(
      caches.match(e.request).then(r => r || fetch(e.request).then(r => { if (r.status === 200) { const c = r.clone(); caches.open(CACHE_NAME).then(cache => cache.put(e.request,c)); } return r; }))
    );
    return;
  }
  e.respondWith(
    fetch(e.request).then(r => { const c = r.clone(); caches.open(CACHE_NAME).then(cache => cache.put(e.request,c)); return r; })
      .catch(() => caches.match(e.request).then(r => r || caches.match(OFFLINE_URL)))
  );
});
