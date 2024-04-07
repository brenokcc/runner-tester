import { openDialog, openIFrameDialog } from "./Modal";
import { appurl } from "./Request";
import { toLabelCase } from "./Utils";

function Link({
  id,
  key,
  href,
  modal,
  imodal,
  children,
  onClick,
  dataLabel,
  style,
}) {
  const url = href && href.indexOf("/media/") < 0 ? appurl(href) : href;

  function onClickDefault(e) {
    e.preventDefault();
    if (modal) openDialog(url);
    else if (imodal) openIFrameDialog(url);
    else window.load(url);
  }

  function render() {
    return (
      <a
        id={id}
        key={key}
        onClick={onClick || onClickDefault}
        href={url || "#"}
        data-label={toLabelCase(dataLabel)}
        style={style}
      >
        {children}
      </a>
    );
  }

  return render();
}

export { Link };
export default Link;
