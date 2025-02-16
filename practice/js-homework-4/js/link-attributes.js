const getAttributes = () => {
  const link = document.getElementById("w3r");
  const attributes = {
    href: link.getAttribute("href"),
    hreflang: link.getAttribute("hreflang"),
    rel: link.getAttribute("rel"),
    target: link.getAttribute("target"),
  };
  console.log(attributes);
};
