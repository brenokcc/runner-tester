function Icons(props) {
  function click(icon) {
    navigator.clipboard.writeText(icon);
  }
  const style1 = { display: "inline-block", width: 150, textAlign: "center" };
  const style2 = { fontSize: "1.5rem" };
  return (
    <div style={{ marginTop: 30 }}>
      {ICONS.map((icon) => (
        <div
          className="icon-box"
          key={Math.random()}
          onClick={() => click(icon)}
          style={style1}
        >
          <i className={"fa-solid fa-fw fa-" + icon}></i>
          <div className="icon-text">{icon}</div>
        </div>
      ))}
    </div>
  );
}

function Icon(props) {
  var className = "fa-solid fa-" + props.icon;
  if (props.className) className += " " + props.className;
  if (props.onClick || props.clickable) className += " clickable";
  return (
    <i style={props.style} className={className} onClick={props.onClick}></i>
  );
}

export { Icon, Icons };
export default Icon;

const ICONS = [
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "fill-drip",
  "arrows-to-circle",
  "circle-chevron-right",
  "at",
  "trash-can",
  "text-height",
  "user-xmark",
  "stethoscope",
  "message",
  "info",
  "down-left-and-up-right-to-center",
  "explosion",
  "file-text",
  "wave-square",
  "ring",
  "building-un",
  "dice-three",
  "calendar-days",
  "anchor-circle-check",
  "building-circle-arrow-right",
  "volleyball",
  "arrows-up-to-line",
  "sort-down",
  "minus-circle",
  "door-open",
  "sign-out-alt",
  "atom",
  "soap",
  "icons",
  "microphone-lines-slash",
  "bridge-circle-check",
  "pump-medical",
  "fingerprint",
  "hand-point-right",
  "search-location",
  "step-forward",
  "smile-beam",
  "flag-checkered",
  "football",
  "school-circle-exclamation",
  "crop",
  "angles-down",
  "users-rectangle",
  "people-roof",
  "people-line",
  "beer",
  "diagram-predecessor",
  "long-arrow-up",
  "fire-flame-simple",
  "person",
  "laptop",
  "file-csv",
  "menorah",
  "truck-plane",
  "record-vinyl",
  "grin-stars",
  "bong",
  "spaghetti-monster-flying",
  "arrow-down-up-across-line",
  "utensil-spoon",
  "jar-wheat",
  "mail-bulk",
  "file-circle-exclamation",
  "hospital-symbol",
  "pager",
  "contact-book",
  "strikethrough",
  "k",
  "landmark-flag",
  "pencil",
  "backward",
  "caret-right",
  "comments",
  "paste",
  "code-pull-request",
  "clipboard-list",
  "truck-ramp-box",
  "user-check",
  "vial-virus",
  "sheet-plastic",
  "blog",
  "user-ninja",
  "person-arrow-up-from-line",
  "torah",
  "quidditch",
  "toggle-off",
  "box-archive",
  "person-drowning",
  "sort-numeric-down-alt",
  "grin-tongue-squint",
  "spray-can",
  "truck-monster",
  "w",
  "globe-africa",
  "rainbow",
  "circle-notch",
  "tablet-screen-button",
  "paw",
  "cloud",
  "trowel-bricks",
  "flushed",
  "hospital-user",
  "tent-arrow-left-right",
  "legal",
  "binoculars",
  "microphone-slash",
  "box-tissue",
  "motorcycle",
  "concierge-bell",
  "pencil-ruler",
  "people-arrows",
  "mars-and-venus-burst",
  "square-caret-right",
  "scissors",
  "sun-plant-wilt",
  "toilets-portable",
  "hockey-puck",
  "table",
  "magnifying-glass-arrow-right",
  "tachograph-digital",
  "users-slash",
  "clover",
  "reply",
  "star-and-crescent",
  "house-fire",
  "square-minus",
  "helicopter",
  "compass",
  "square-caret-down",
  "file-circle-question",
  "laptop-code",
  "swatchbook",
  "prescription-bottle",
  "navicon",
  "people-group",
  "hourglass-end",
  "heart-crack",
  "square-up-right",
  "kiss-beam",
  "film",
  "ruler-horizontal",
  "people-robbery",
  "lightbulb",
  "caret-left",
  "exclamation-circle",
  "school-circle-xmark",
  "sign-out",
  "circle-chevron-down",
  "unlock-keyhole",
  "cloud-showers-heavy",
  "headphones-simple",
  "sitemap",
  "donate",
  "memory",
  "road-spikes",
  "fire-burner",
  "flag",
  "hanukiah",
  "feather",
  "volume-low",
  "comment-slash",
  "cloud-sun-rain",
  "compress",
  "wheat-awn",
  "ankh",
  "hands-holding-child",
  "asterisk",
  "square-check",
  "peseta-sign",
  "heading",
  "ghost",
  "list",
  "square-phone-flip",
  "cart-plus",
  "gamepad",
  "dot-circle",
  "face-dizzy",
  "egg",
  "house-medical-circle-xmark",
  "campground",
  "folder-plus",
  "soccer-ball",
  "paintbrush",
  "lock",
  "gas-pump",
  "hot-tub",
  "map-marked",
  "house-flood-water",
  "tree",
  "bridge-lock",
  "sack-dollar",
  "pen-to-square",
  "car-side",
  "share-nodes",
  "heart-circle-minus",
  "hourglass-half",
  "microscope",
  "sink",
  "shopping-bag",
  "sort-alpha-down-alt",
  "mitten",
  "person-rays",
  "users",
  "eye-slash",
  "flask-vial",
  "hand",
  "om",
  "worm",
  "house-circle-xmark",
  "plug",
  "chevron-up",
  "hand-spock",
  "stopwatch",
  "kiss",
  "bridge-circle-xmark",
  "grin-tongue",
  "chess-bishop",
  "grin-wink",
  "hard-of-hearing",
  "road-circle-check",
  "dice-five",
  "square-rss",
  "land-mine-on",
  "i-cursor",
  "stamp",
  "stairs",
  "i",
  "hryvnia",
  "pills",
  "grin-alt",
  "tooth",
  "v",
  "bangladeshi-taka-sign",
  "bicycle",
  "staff-snake",
  "head-side-cough-slash",
  "truck-medical",
  "wheat-awn-circle-exclamation",
  "snowman",
  "mortar-pestle",
  "road-barrier",
  "school",
  "igloo",
  "joint",
  "angle-right",
  "horse",
  "q",
  "g",
  "notes-medical",
  "thermometer-half",
  "dong-sign",
  "capsules",
  "poo-storm",
  "frown-open",
  "hand-point-up",
  "money-bill",
  "bookmark",
  "align-justify",
  "umbrella-beach",
  "helmet-un",
  "bullseye",
  "bacon",
  "hand-point-down",
  "arrow-up-from-bracket",
  "folder",
  "file-waveform",
  "radiation",
  "chart-simple",
  "mars-stroke",
  "vial",
  "tachometer-alt-average",
  "wand-magic-sparkles",
  "e",
  "pen-clip",
  "bridge-circle-exclamation",
  "user",
  "school-circle-check",
  "dumpster",
  "van-shuttle",
  "building-user",
  "square-caret-left",
  "highlighter",
  "key",
  "bullhorn",
  "globe",
  "synagogue",
  "person-half-dress",
  "road-bridge",
  "location-arrow",
  "c",
  "tablet-button",
  "building-lock",
  "pizza-slice",
  "money-bill-wave",
  "chart-area",
  "house-flag",
  "person-circle-minus",
  "cancel",
  "camera-rotate",
  "spray-can-sparkles",
  "star",
  "repeat",
  "cross",
  "box",
  "venus-mars",
  "mouse-pointer",
  "maximize",
  "charging-station",
  "triangle-circle-square",
  "shuffle",
  "running",
  "mobile-retro",
  "grip-lines-vertical",
  "spider",
  "hands-bound",
  "file-invoice-dollar",
  "plane-circle-exclamation",
  "x-ray",
  "spell-check",
  "slash",
  "mouse",
  "sign-in",
  "store-alt-slash",
  "server",
  "virus-covid-slash",
  "shop-lock",
  "hourglass-start",
  "blender-phone",
  "building-wheat",
  "person-breastfeeding",
  "sign-in-alt",
  "venus",
  "passport",
  "heartbeat",
  "people-carry",
  "temperature-high",
  "microchip",
  "crown",
  "weight-hanging",
  "xmarks-lines",
  "file-prescription",
  "weight",
  "user-group",
  "sort-alpha-up",
  "chess-knight",
  "laugh-squint",
  "wheelchair",
  "circle-arrow-up",
  "toggle-on",
  "walking",
  "l",
  "fire",
  "procedures",
  "space-shuttle",
  "laugh",
  "folder-open",
  "heart-circle-plus",
  "code-fork",
  "city",
  "microphone-lines",
  "pepper-hot",
  "unlock",
  "colon-sign",
  "headset",
  "store-slash",
  "road-circle-xmark",
  "user-minus",
  "mars-stroke-v",
  "glass-cheers",
  "clipboard",
  "house-circle-exclamation",
  "file-upload",
  "wifi",
  "bathtub",
  "underline",
  "user-pen",
  "signature",
  "stroopwafel",
  "bold",
  "anchor-lock",
  "building-ngo",
  "manat-sign",
  "not-equal",
  "border-top-left",
  "map-marked-alt",
  "jedi",
  "square-poll-vertical",
  "mug-hot",
  "car-battery",
  "gift",
  "dice-two",
  "chess-queen",
  "glasses",
  "chess-board",
  "building-circle-check",
  "person-chalkboard",
  "mars-stroke-right",
  "hand-rock",
  "square-caret-up",
  "cloud-showers-water",
  "chart-bar",
  "hands-wash",
  "less-than-equal",
  "train",
  "low-vision",
  "crow",
  "sailboat",
  "window-restore",
  "square-plus",
  "torii-gate",
  "frog",
  "bucket",
  "image",
  "microphone",
  "cow",
  "caret-up",
  "screwdriver",
  "folder-closed",
  "house-tsunami",
  "square-nfi",
  "arrow-up-from-ground-water",
  "martini-glass",
  "undo-alt",
  "table-columns",
  "lemon",
  "head-side-mask",
  "handshake",
  "gem",
  "dolly",
  "smoking",
  "minimize",
  "monument",
  "snowplow",
  "angles-right",
  "cannabis",
  "play-circle",
  "tablets",
  "ethernet",
  "euro",
  "chair",
  "circle-check",
  "stop-circle",
  "drafting-compass",
  "plate-wheat",
  "icicles",
  "person-shelter",
  "neuter",
  "id-badge",
  "marker",
  "laugh-beam",
  "helicopter-symbol",
  "universal-access",
  "circle-chevron-up",
  "lari-sign",
  "volcano",
  "person-walking-dashed-line-arrow-right",
  "sterling-sign",
  "viruses",
  "square-person-confined",
  "user-tie",
  "long-arrow-down",
  "tent-arrow-down-to-line",
  "certificate",
  "reply-all",
  "suitcase",
  "skating",
  "funnel-dollar",
  "camera-retro",
  "circle-arrow-down",
  "file-import",
  "square-arrow-up-right",
  "box-open",
  "scroll",
  "spa",
  "location-pin-lock",
  "pause",
  "hill-avalanche",
  "thermometer-empty",
  "bomb",
  "registered",
  "vcard",
  "scale-unbalanced-flip",
  "subscript",
  "directions",
  "burst",
  "laptop-house",
  "tired",
  "money-bills",
  "smog",
  "crutch",
  "cloud-upload",
  "palette",
  "arrows-turn-right",
  "vest",
  "ferry",
  "arrows-down-to-people",
  "sprout",
  "left-right",
  "boxes-packing",
  "circle-arrow-left",
  "group-arrows-rotate",
  "bowl-food",
  "candy-cane",
  "sort-amount-down",
  "thunderstorm",
  "text-slash",
  "smile-wink",
  "file-word",
  "file-powerpoint",
  "arrows-left-right",
  "house-lock",
  "cloud-download",
  "children",
  "chalkboard",
  "user-large-slash",
  "envelope-open",
  "handshake-simple-slash",
  "mattress-pillow",
  "guarani-sign",
  "sync",
  "fire-extinguisher",
  "cruzeiro-sign",
  "greater-than-equal",
  "shield-halved",
  "book-atlas",
  "virus",
  "envelope-circle-check",
  "layer-group",
  "arrows-to-dot",
  "archway",
  "heart-circle-check",
  "house-damage",
  "file-zipper",
  "square",
  "martini-glass-empty",
  "couch",
  "cedi-sign",
  "italic",
  "church",
  "comments-dollar",
  "democrat",
  "z",
  "skiing",
  "road-lock",
  "a",
  "temperature-down",
  "feather-pointed",
  "p",
  "snowflake",
  "newspaper",
  "rectangle-ad",
  "circle-arrow-right",
  "filter-circle-xmark",
  "locust",
  "unsorted",
  "list-ol",
  "person-dress-burst",
  "money-check-dollar",
  "vector-square",
  "bread-slice",
  "language",
  "kiss-wink-heart",
  "filter",
  "question",
  "file-signature",
  "up-down-left-right",
  "house-chimney-user",
  "hand-holding-heart",
  "puzzle-piece",
  "money-check",
  "star-half-stroke",
  "code",
  "whiskey-glass",
  "building-circle-exclamation",
  "magnifying-glass-chart",
  "external-link",
  "cubes-stacked",
  "won",
  "virus-covid",
  "austral-sign",
  "f",
  "leaf",
  "road",
  "taxi",
  "person-circle-plus",
  "pie-chart",
  "bolt-lightning",
  "sack-xmark",
  "file-excel",
  "file-contract",
  "fish-fins",
  "building-flag",
  "grin-beam",
  "object-ungroup",
  "poop",
  "map-marker",
  "kaaba",
  "toilet-paper",
  "helmet-safety",
  "eject",
  "circle-right",
  "plane-circle-check",
  "meh-rolling-eyes",
  "object-group",
  "line-chart",
  "mask-ventilator",
  "arrow-right",
  "signs-post",
  "cash-register",
  "person-circle-question",
  "h",
  "tarp",
  "tools",
  "arrows-to-eye",
  "plug-circle-bolt",
  "heart",
  "mars-and-venus",
  "house-user",
  "dumpster-fire",
  "house-crack",
  "martini-glass-citrus",
  "surprise",
  "bottle-water",
  "pause-circle",
  "toilet-paper-slash",
  "apple-whole",
  "kitchen-set",
  "r",
  "thermometer-quarter",
  "cube",
  "bitcoin-sign",
  "shield-dog",
  "solar-panel",
  "lock-open",
  "elevator",
  "money-bill-transfer",
  "money-bill-trend-up",
  "house-flood-water-circle-arrow-right",
  "square-poll-horizontal",
  "circle",
  "fast-backward",
  "recycle",
  "user-astronaut",
  "plane-slash",
  "trademark",
  "basketball",
  "satellite-dish",
  "circle-up",
  "mobile-screen-button",
  "volume-up",
  "users-rays",
  "wallet",
  "clipboard-check",
  "file-audio",
  "hamburger",
  "wrench",
  "bugs",
  "rupee",
  "file-image",
  "question-circle",
  "plane-departure",
  "handshake-slash",
  "book-bookmark",
  "code-branch",
  "hat-cowboy",
  "bridge",
  "phone-flip",
  "truck-front",
  "cat",
  "anchor-circle-exclamation",
  "truck-field",
  "route",
  "clipboard-question",
  "panorama",
  "comment-medical",
  "teeth-open",
  "file-circle-minus",
  "tags",
  "wine-glass",
  "fast",
  "meh-blank",
  "square-parking",
  "house-signal",
  "tasks-alt",
  "faucet-drip",
  "dolly-flatbed",
  "smoking-ban",
  "terminal",
  "mobile-button",
  "house-medical-flag",
  "shopping-basket",
  "tape",
  "bus-simple",
  "eye",
  "sad-cry",
  "audio-description",
  "person-military-to-person",
  "file-shield",
  "user-slash",
  "pen",
  "tower-observation",
  "file-code",
  "signal",
  "bus",
  "heart-circle-xmark",
  "house-chimney",
  "window-maximize",
  "frown",
  "prescription",
  "store-alt",
  "save",
  "vihara",
  "scale-unbalanced",
  "sort-up",
  "commenting",
  "plant-wilt",
  "diamond",
  "grin-squint",
  "hand-holding-usd",
  "bacterium",
  "hand-pointer",
  "drum-steelpan",
  "hand-scissors",
  "praying-hands",
  "redo",
  "biohazard",
  "location",
  "mars-double",
  "child-dress",
  "users-between-lines",
  "lungs-virus",
  "grin-tears",
  "phone",
  "calendar-xmark",
  "child-reaching",
  "head-side-virus",
  "user-gear",
  "sort-numeric-up",
  "door-closed",
  "shield-virus",
  "dice-six",
  "mosquito-net",
  "bridge-water",
  "person-booth",
  "text-width",
  "hat-wizard",
  "fancy",
  "person-digging",
  "trash",
  "tachometer-average",
  "book-medical",
  "poo",
  "quote-right",
  "tshirt",
  "cubes",
  "divide",
  "tenge",
  "headphones",
  "hands-holding",
  "hands-clapping",
  "republican",
  "arrow-left",
  "person-circle-xmark",
  "ruler",
  "align-left",
  "dice-d6",
  "restroom",
  "j",
  "users-viewfinder",
  "file-video",
  "up-right-from-square",
  "th",
  "file-pdf",
  "book-bible",
  "o",
  "suitcase-medical",
  "user-secret",
  "otter",
  "person-dress",
  "comment-dollar",
  "business-time",
  "th-large",
  "tanakh",
  "volume-control-phone",
  "hat-cowboy-side",
  "clipboard-user",
  "child",
  "lira-sign",
  "satellite",
  "plane-lock",
  "tag",
  "comment",
  "cake",
  "envelope",
  "angles-up",
  "paperclip",
  "arrow-right-to-city",
  "ribbon",
  "lungs",
  "sort-numeric-up-alt",
  "litecoin-sign",
  "border-none",
  "circle-nodes",
  "parachute-box",
  "indent",
  "truck-field-un",
  "hourglass",
  "mountain",
  "user-md",
  "info-circle",
  "cloud-meatball",
  "camera",
  "square-virus",
  "meteor",
  "car-on",
  "sleigh",
  "sort-numeric-down",
  "hand-holding-water",
  "water",
  "calendar-check",
  "braille",
  "prescription-bottle-medical",
  "landmark",
  "truck",
  "crosshairs",
  "person-cane",
  "tent",
  "vest-patches",
  "check-double",
  "sort-alpha-down",
  "money-bill-wheat",
  "cookie",
  "undo",
  "hdd",
  "grin-squint-tears",
  "dumbbell",
  "rectangle-list",
  "tarp-droplet",
  "house-medical-circle-check",
  "skiing-nordic",
  "calendar-plus",
  "plane-arrival",
  "circle-left",
  "train-subway",
  "chart-gantt",
  "inr",
  "crop-simple",
  "money-bill-alt",
  "long-arrow-alt-left",
  "dna",
  "virus-slash",
  "subtract",
  "chess",
  "long-arrow-left",
  "plug-circle-check",
  "street-view",
  "franc-sign",
  "volume-off",
  "hands-asl-interpreting",
  "gear",
  "tint-slash",
  "mosque",
  "mosquito",
  "star-of-david",
  "person-military-rifle",
  "shopping-cart",
  "vials",
  "plug-circle-plus",
  "place-of-worship",
  "grip-vertical",
  "level-up",
  "u",
  "square-root-variable",
  "clock",
  "step-backward",
  "pallet",
  "faucet",
  "baseball-bat-ball",
  "s",
  "timeline",
  "keyboard",
  "caret-down",
  "house-chimney-medical",
  "thermometer-three-quarters",
  "mobile-screen",
  "plane-up",
  "piggy-bank",
  "battery-half",
  "mountain-city",
  "coins",
  "khanda",
  "sliders",
  "folder-tree",
  "network-wired",
  "map-pin",
  "hamsa",
  "cent-sign",
  "flask",
  "person-pregnant",
  "wand-sparkles",
  "ellipsis-vertical",
  "ticket",
  "power-off",
  "right-long",
  "flag-usa",
  "laptop-file",
  "tty",
  "diagram-next",
  "person-rifle",
  "house-medical-circle-exclamation",
  "closed-captioning",
  "person-hiking",
  "venus-double",
  "images",
  "calculator",
  "people-pulling",
  "n",
  "tram",
  "cloud-rain",
  "building-circle-xmark",
  "ship",
  "arrows-down-to-line",
  "download",
  "grin",
  "delete-left",
  "eyedropper",
  "file-circle-check",
  "forward",
  "mobile",
  "meh",
  "align-center",
  "book-skull",
  "id-card",
  "outdent",
  "heart-circle-exclamation",
  "house",
  "calendar-week",
  "laptop-medical",
  "b",
  "file-medical",
  "dice-one",
  "kiwi-bird",
  "exchange",
  "rotate-right",
  "utensils",
  "sort-amount-up",
  "mill-sign",
  "bowl-rice",
  "skull",
  "tower-broadcast",
  "truck-pickup",
  "up-long",
  "stop",
  "code-merge",
  "upload",
  "hurricane",
  "mound",
  "toilet-portable",
  "compact-disc",
  "file-download",
  "caravan",
  "shield-cat",
  "zap",
  "glass-water",
  "oil-well",
  "vault",
  "mars",
  "toilet",
  "plane-circle-xmark",
  "yen",
  "ruble",
  "sun",
  "guitar",
  "laugh-wink",
  "horse-head",
  "bore-hole",
  "industry",
  "circle-down",
  "arrows-turn-to-dots",
  "florin-sign",
  "sort-amount-down-alt",
  "less-than",
  "angle-down",
  "car-tunnel",
  "head-side-cough",
  "grip-lines",
  "thumbs-down",
  "user-lock",
  "long-arrow-right",
  "anchor-circle-xmark",
  "ellipsis",
  "chess-pawn",
  "kit-medical",
  "person-through-window",
  "toolbox",
  "hands-holding-circle",
  "bug",
  "credit-card",
  "car",
  "hand-holding-hand",
  "book-reader",
  "mountain-sun",
  "arrows-left-right-to-line",
  "dice-d20",
  "truck-droplet",
  "file-circle-xmark",
  "temperature-up",
  "medal",
  "bed",
  "square-h",
  "podcast",
  "thermometer-full",
  "bell",
  "superscript",
  "plug-circle-xmark",
  "star-of-life",
  "phone-slash",
  "paint-roller",
  "handshake-angle",
  "map-marker-alt",
  "file",
  "greater-than",
  "swimmer",
  "arrow-down",
  "tint",
  "eraser",
  "globe-americas",
  "person-burst",
  "dove",
  "battery-empty",
  "socks",
  "inbox",
  "section",
  "tachometer-alt",
  "envelope-open-text",
  "hospital",
  "wine-bottle",
  "chess-rook",
  "stream",
  "dharmachakra",
  "hotdog",
  "person-walking-with-cane",
  "drum",
  "ice-cream",
  "heart-circle-bolt",
  "fax",
  "paragraph",
  "vote-yea",
  "star-half",
  "boxes",
  "link",
  "ear-listen",
  "tree-city",
  "play",
  "font",
  "rupiah-sign",
  "search",
  "table-tennis",
  "person-dots-from-line",
  "trash-restore-alt",
  "naira-sign",
  "cart-arrow-down",
  "walkie-talkie",
  "file-pen",
  "receipt",
  "square-pen",
  "suitcase-rolling",
  "person-circle-exclamation",
  "chevron-down",
  "battery",
  "skull-crossbones",
  "code-compare",
  "list-ul",
  "school-lock",
  "tower-cell",
  "long-arrow-alt-down",
  "ranking-star",
  "chess-king",
  "person-harassing",
  "brazilian-real-sign",
  "landmark-dome",
  "arrow-up",
  "tv",
  "shrimp",
  "tasks",
  "jug-detergent",
  "user-circle",
  "user-shield",
  "wind",
  "car-crash",
  "y",
  "snowboarding",
  "fast",
  "fish",
  "user-graduate",
  "circle-half-stroke",
  "clapperboard",
  "radiation-alt",
  "baseball",
  "jet-fighter-up",
  "project-diagram",
  "copy",
  "volume-xmark",
  "hand-sparkles",
  "grip",
  "share-square",
  "child-rifle",
  "gun",
  "square-phone",
  "plus",
  "expand",
  "computer",
  "xmark",
  "arrows",
  "chalkboard-user",
  "peso-sign",
  "building-shield",
  "baby",
  "users-line",
  "quote-left",
  "tractor",
  "trash-restore",
  "arrow-down-up-lock",
  "lines-leaning",
  "ruler-combined",
  "copyright",
  "equals",
  "blender",
  "teeth",
  "sheqel",
  "map",
  "rocket",
  "photo-video",
  "folder-minus",
  "store",
  "arrow-trend-up",
  "plug-circle-minus",
  "sign",
  "bezier-curve",
  "bell-slash",
  "tablet",
  "school-flag",
  "fill",
  "angle-up",
  "drumstick-bite",
  "holly-berry",
  "chevron-left",
  "bacteria",
  "hand-lizard",
  "notdef",
  "disease",
  "briefcase-medical",
  "genderless",
  "chevron-right",
  "retweet",
  "car-rear",
  "pump-soap",
  "video-slash",
  "battery-quarter",
  "radio",
  "carriage-baby",
  "traffic-light",
  "thermometer",
  "vr-cardboard",
  "hand-middle-finger",
  "percentage",
  "truck-moving",
  "glass-water-droplet",
  "display",
  "smile",
  "thumbtack",
  "trophy",
  "pray",
  "hammer",
  "hand-peace",
  "sync-alt",
  "spinner",
  "robot",
  "peace",
  "gears",
  "warehouse",
  "arrow-up-right-dots",
  "splotch",
  "grin-hearts",
  "dice-four",
  "sim-card",
  "transgender",
  "mercury",
  "level-down",
  "falling-burst",
  "award",
  "ticket-simple",
  "building",
  "angles-left",
  "qrcode",
  "history",
  "grin-beam-sweat",
  "file-export",
  "shield",
  "sort-amount-up-alt",
  "house-medical",
  "golf-ball",
  "circle-chevron-left",
  "house-chimney-window",
  "pen-nib",
  "tent-arrow-turn-left",
  "tents",
  "wand-magic",
  "dog",
  "carrot",
  "moon",
  "wine-glass-empty",
  "cheese",
  "yin-yang",
  "music",
  "code-commit",
  "temperature-low",
  "person-biking",
  "broom",
  "shield-heart",
  "gopuram",
  "globe-oceania",
  "xmark-square",
  "hashtag",
  "up-right-and-down-left-from-center",
  "oil-can",
  "t",
  "hippo",
  "chart-column",
  "infinity",
  "vial-circle-check",
  "person-arrow-down-to-line",
  "voicemail",
  "fan",
  "person-walking-luggage",
  "up-down",
  "cloud-moon-rain",
  "calendar",
  "trailer",
  "haykal",
  "sd-card",
  "dragon",
  "shoe-prints",
  "plus-circle",
  "grin-tongue-wink",
  "hand-holding",
  "plug-circle-exclamation",
  "unlink",
  "clone",
  "person-walking-arrow-loop-left",
  "sort-alpha-up-alt",
  "fire-flame-curved",
  "tornado",
  "file-circle-plus",
  "quran",
  "anchor",
  "border-all",
  "face-angry",
  "cookie-bite",
  "arrow-trend-down",
  "rss",
  "draw-polygon",
  "scale-balanced",
  "tachometer",
  "shower",
  "desktop",
  "m",
  "th-list",
  "sms",
  "book",
  "user-plus",
  "check",
  "battery-three-quarters",
  "house-circle-check",
  "angle-left",
  "diagram-successor",
  "truck-arrow-right",
  "arrows-split-up-and-left",
  "hand-fist",
  "cloud-moon",
  "briefcase",
  "falling",
  "portrait",
  "user-tag",
  "rug",
  "globe-europe",
  "luggage-cart",
  "window-close",
  "baht-sign",
  "book-open",
  "journal-whills",
  "handcuffs",
  "warning",
  "database",
  "share",
  "bottle-droplet",
  "face",
  "hill-rockslide",
  "right-left",
  "paper-plane",
  "road-circle-exclamation",
  "dungeon",
  "align-right",
  "money-bill-wave-alt",
  "life-ring",
  "signing",
  "calendar-day",
  "water-ladder",
  "arrows-v",
  "grimace",
  "wheelchair-move",
  "turn-down",
  "person-walking-arrow-right",
  "square-envelope",
  "dice",
  "bowling-ball",
  "brain",
  "bandage",
  "calendar-minus",
  "xmark-circle",
  "gifts",
  "hotel",
  "globe-asia",
  "id-card-clip",
  "search-plus",
  "thumbs-up",
  "user-clock",
  "hand-dots",
  "file-invoice",
  "window-minimize",
  "mug-saucer",
  "brush",
  "mask",
  "search-minus",
  "ruler-vertical",
  "user-large",
  "train-tram",
  "user-nurse",
  "syringe",
  "cloud-sun",
  "stopwatch-20",
  "square-full",
  "magnet",
  "jar",
  "sticky-note",
  "bug-slash",
  "arrow-up-from-water-pump",
  "bone",
  "user-injured",
  "sad-tear",
  "plane",
  "tent-arrows-down",
  "exclamation",
  "arrows-spin",
  "print",
  "turkish-lira",
  "usd",
  "x",
  "search-dollar",
  "users-gear",
  "person-military-pointing",
  "university",
  "umbrella",
  "trowel",
  "d",
  "stapler",
  "theater-masks",
  "kip-sign",
  "hand-point-left",
  "handshake-simple",
  "jet-fighter",
  "square-share-nodes",
  "barcode",
  "plus-minus",
  "video",
  "mortar-board",
  "hand-holding-medical",
  "person-circle-check",
  "turn-up",
];
