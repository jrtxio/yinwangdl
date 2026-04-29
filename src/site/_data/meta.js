require("dotenv").config();

module.exports = () => ({
  siteName: process.env.SITE_NAME || "王垠博客备份",
  siteBaseUrl: process.env.SITE_BASE_URL || "",
  mainLanguage: process.env.SITE_MAIN_LANGUAGE || "zh",
  adsenseClient: process.env.GOOGLE_ADSENSE_CLIENT || "",
  adsenseSlot: process.env.GOOGLE_ADSENSE_SLOT || "",
  buildDate: new Date(),
});
