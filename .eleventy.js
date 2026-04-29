require("dotenv").config();

module.exports = function (eleventyConfig) {
  // Passthrough copies
  eleventyConfig.addPassthroughCopy("images");
  eleventyConfig.addPassthroughCopy("src/site/styles");
  eleventyConfig.addPassthroughCopy("src/site/ads.txt");
  eleventyConfig.addPassthroughCopy("src/site/robots.txt");

  // Date formatting filter
  eleventyConfig.addFilter("isodate", (date) => {
    if (!date) return "";
    if (typeof date === "string") return date.substring(0, 10);
    if (date instanceof Date) return date.toISOString().substring(0, 10);
    return String(date).substring(0, 10);
  });

  // Sort posts by created date descending
  eleventyConfig.addCollection("post", function (collectionApi) {
    return collectionApi
      .getFilteredByTag("post")
      .sort((a, b) => {
        const dateA = String(a.data.created || "0000");
        const dateB = String(b.data.created || "0000");
        return dateB.localeCompare(dateA);
      });
  });

  return {
    dir: {
      input: ".",
      output: "dist",
      includes: "src/site/_includes",
      data: "src/site/_data",
    },
    templateFormats: ["njk", "md"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
    passthroughFileCopy: true,
  };
};
