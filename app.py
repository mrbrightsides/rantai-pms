import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RANTAI PMS",
    page_icon="🏨",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **RANTAI PMS** adalah sistem manajemen properti modern yang dirancang untuk hotel, resort, dan properti hospitality lainnya. Platform ini mengintegrasikan seluruh aspek operasional—mulai dari reservasi, front desk, housekeeping, maintenance, hingga billing dan analytics—dalam satu sistem terpadu.

    Dengan Rantai-PMS, pengelola properti bisa:
    
    - Mengotomasi proses check-in/out dan manajemen kamar secara real-time.
    
    - Meningkatkan efisiensi staf melalui mobile apps dan notifikasi otomatis.
    
    - Memperoleh data analitik lengkap untuk pengambilan keputusan berbasis performa.
    
    ---
    #### 🔮 Vision Statement
    
    Visi kami adalah menjadi platform PMS terdepan yang mendukung operasional properti hospitality secara efisien, modern, dan berkelanjutan.

    Kami bertujuan untuk:
    
    - Menjadi solusi end-to-end bagi pengelola properti dalam menghadapi tantangan operasional dan manajemen.
    
    - Memberikan pengalaman tamu yang nyaman, cepat, dan personal melalui digitalisasi layanan.
    
    - Mendukung praktik hospitality berkelanjutan dengan monitoring energi, green compliance, dan pelaporan ESG.
    
    - Mempermudah pengambilan keputusan bisnis melalui data analytics dan dashboard intuitif.
   
    ---
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/rantai-pms)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

# URL Ohara
iframe_url = "https://pms.elpeef.com"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=0, hide_bottom_px = -105, height=800)
