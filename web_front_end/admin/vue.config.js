module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/static/manage/" : "/",
  outputDir: process.env.NODE_ENV === "production" ? "dist/manage" : "dist"
};
