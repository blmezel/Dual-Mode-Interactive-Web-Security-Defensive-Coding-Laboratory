// Güvenlik Loglarındaki HTTP Statü Kodlarını Ayrıştıran Script
function parseAuditLogs(logLine) {
    if (logLine.includes("423")) return "ACCOUNT_LOCKED";
    if (logLine.includes("429")) return "RATE_LIMIT_EXCEEDED";
    if (logLine.includes("403")) return "AUTHENTICATION_FORBIDDEN";
    return "TRAFFIC_CLEAN";
}
