const CACHE = 'navcalc-v2';
const URLS = [
  '/',
  '/navcalc/',
  '/navcalc/index.html',
  '/navcalc/manifest.json',
  '/navcalc/offline.html',
  '/navcalc/icons/icon-72x72.png',
  '/navcalc/icons/icon-96x96.png',
  '/navcalc/icons/icon-128x128.png',
  '/navcalc/icons/icon-144x144.png',
  '/navcalc/icons/icon-152x152.png',
  '/navcalc/icons/icon-192x192.png',
  '/navcalc/icons/icon-384x384.png',
  '/navcalc/icons/icon-512x512.png'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(URLS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request).then(res => {
      if (res.ok && res.type === 'basic') {
        const clone = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, clone));
      }
      return res;
    }).catch(() => caches.match('/navcalc/offline.html')))
  );
});
