// SecureSphere Canlı Metrik Takip Betiği
const metrics = {
    totalRequests: 0,
    blockedAttacks: 0,
    lastHttpStatusCode: 200
};

function updateSecOpsDashboard(status) {
    if (status === 403 || status === 423) {
        metrics.blockedAttacks++;
        console.warn(`[ALERT] Siber Güvenlik Kalkanı Tetiklendi: HTTP ${status}`);
    }
}
