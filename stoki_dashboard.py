import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Stoki Market Entry Strategy",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1E3A8A;
    font-weight: 800;
    background: linear-gradient(90deg, #1E3A8A, #3B82F6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.sub-header {
    font-size: 1.3rem;
    color: #4B5563;
    margin-bottom: 2rem;
}
.strategy-card {
    background: white;
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 5px solid #3B82F6;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    margin: 1rem 0;
}
.metric-highlight {
    background: linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%);
    color: white;
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.competitor-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.1rem;
}
.insight-box {
    background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
    border: 1px solid #BAE6FD;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🚀 Stoki Market Entry Strategy</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Medium-Level Analysis for SA SMME FinTech Market Entry</p>', unsafe_allow_html=True)

# Generate synthetic data
def generate_stoki_data():
    # Market fundamentals
    market_fundamentals = pd.DataFrame({
        'Metric': ['Total Addressable Market (TAM)', 'Serviceable Addressable Market (SAM)', 
                   'Serviceable Obtainable Market (SOM)', 'Current Market Penetration'],
        'Value': [750000, 250000, 40000, 16000],
        'Unit': ['SMMEs', 'SMMEs', 'SMMEs', 'SMMEs'],
        'Description': ['Total SA SMMEs with internet', 'Metro SMMEs > R1M turnover', 
                       'Year 1-3 Target (16% of SAM)', 'Currently using digital tools']
    })
    
    # Competitor financial data
    competitors_data = pd.DataFrame({
        'Company': ['Invoicely', 'ZazuPay', 'SA-Books', 'QuickStoki', 'CapitFlow', 'Stoki (Target)'],
        'Revenue_Q2_2024_R_M': [2.5, 1.7, 1.7, 1.4, 1.4, 0.0],
        'Market_Share': [25.8, 17.5, 17.5, 14.4, 14.4, 0.0],
        'YoY_Growth': [66.7, 54.5, 13.3, 40.0, 133.3, 0.0],
        'Customers': [8200, 6500, 9000, 12000, 3500, 0],
        'ARPU_Monthly': [305, 262, 189, 117, 400, 349],
        'CAC': [800, 650, 400, 250, 1200, 550],
        'Funding_Raised_R_M': [18.0, 8.5, 5.0, 0, 22.0, 0],
        'Valuation_R_M': [95.0, 45.0, 35.0, 25.0, 120.0, 0]
    })
    
    # Calculate profitability
    competitors_data['Profit_Margin'] = [28.1, 15.0, 14.7, 35.7, 10.7, 0]
    competitors_data['CAC_Payback_Months'] = competitors_data['CAC'] / competitors_data['ARPU_Monthly']
    
    # Feature matrix
    features = pd.DataFrame({
        'Feature': ['Invoicing', 'Expense Tracking', 'Cashflow Forecasting', 
                   'VAT Submission', 'Bank Integration', 'Beautiful UX', 'Mobile App'],
        'Invoicely': [1, 1, 0, 1, 1, 0, 1],
        'ZazuPay': [1, 1, 0, 0, 0, 1, 1],
        'SA-Books': [1, 1, 0, 1, 1, 0, 0],
        'QuickStoki': [1, 0, 0, 0, 0, 0, 1],
        'CapitFlow': [0, 0, 1, 0, 1, 1, 1],
        'Stoki': [1, 1, 1, 1, 1, 1, 1]
    })
    
    # Competitive positioning
    positioning = pd.DataFrame({
        'Company': ['QuickStoki', 'ZazuPay', 'SA-Books', 'CapitFlow', 'Invoicely', 'Stoki (Target)'],
        'X_Feature_Score': [2.1, 6.8, 5.5, 8.2, 7.0, 8.5],
        'Y_Price_Index': [2.0, 4.5, 7.9, 8.9, 6.0, 5.0],
        'Bubble_Size_Customers': [12000, 6500, 9000, 3500, 8200, 0],
        'Quadrant': ['Budget-Basic', 'Value-Advanced', 'Premium-Complex', 
                    'Premium-Complex', 'Premium-Complex', 'Value-Advanced']
    })
    
    # Target segments
    segments = pd.DataFrame({
        'Segment': ['Micro (1-10 employees)', 'Small (11-50 employees)', 'Medium (51-200 employees)'],
        'Market_Size': [65, 30, 5],
        'Current_Digital_Adoption': [12, 25, 40],
        'ARPU_Potential': [150, 349, 699],
        'CAC': [200, 550, 1200],
        'Growth_Rate': [20, 35, 15]
    })
    
    # Initial results
    results = pd.DataFrame({
        'Metric': ['Business Signups (Q1)', 'Monthly Recurring Revenue (MRR)', 
                  'Customer Acquisition Cost (CAC)', 'CAC Payback Period',
                  'Customer Satisfaction', 'Feature Development Progress'],
        'Current': [217, 75000, 520, 6.2, 4.2, 70],
        'Target': [200, 100000, 600, 9, 4.5, 100],
        'Unit': ['businesses', 'R/month', 'R', 'months', '/5.0', '%']
    })
    
    # Pain points analysis
    pain_points = pd.DataFrame({
        'Pain_Point': ['Late payments from clients', 'Time spent on admin/invoicing/VAT',
                      'Understanding cash flow', 'Paying suppliers'],
        'Prevalence': [45, 30, 15, 10],
        'Addressed_by_Stoki': [True, True, True, False],
        'Priority': [1, 1, 1, 2]
    })
    
    return market_fundamentals, competitors_data, features, positioning, segments, results, pain_points

# Load data
market_fundamentals, competitors_data, features, positioning, segments, results, pain_points = generate_stoki_data()

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2694/2694920.png", width=80)
    st.title("Stoki Strategy Console")
    st.markdown("---")
    
    analysis_focus = st.selectbox(
        "Analysis Focus",
        ["Market Overview", "Competitive Landscape", "Target Segmentation", 
         "Positioning Strategy", "Performance Tracker", "Go-to-Market Plan"]
    )
    
    st.markdown("---")
    st.markdown("### 💡 Key Insights")
    st.success("**Sweet Spot Identified:** Businesses with 11-50 employees")
    st.info("**Optimal Pricing:** R349/month")
    st.warning("**Key Differentiator:** Beautiful UX + Cashflow Automation")
    
    st.markdown("---")
    st.markdown("### 🎯 Quick Stats")
    st.metric("Target SOM", "40,000 SMMEs")
    st.metric("Projected ARPU", "R349/month")
    st.metric("Target CAC", "R550")
    st.metric("Q1 Signups", "217", "17")

# Main content based on selected focus
if analysis_focus == "Market Overview":
    st.header("🌍 Market Opportunity Analysis")
    
    # Market metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-highlight">', unsafe_allow_html=True)
        st.metric(
            "Total Addressable Market",
            "750,000",
            "SMMEs"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-highlight">', unsafe_allow_html=True)
        st.metric(
            "Serviceable Market",
            "250,000",
            "Metro SMMEs"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-highlight">', unsafe_allow_html=True)
        st.metric(
            "Obtainable Market",
            "40,000",
            "Year 1-3 Target"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-highlight">', unsafe_allow_html=True)
        st.metric(
            "Current Digital Adoption",
            "16,000",
            "6.4% of SAM"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Market funnel visualization
    st.subheader("📊 Market Funnel Analysis")
    
    fig = go.Figure(go.Funnel(
        y = ["TAM (750,000)", "SAM (250,000)", "SOM (40,000)", "Current (16,000)"],
        x = [750000, 250000, 40000, 16000],
        textposition = "inside",
        textinfo = "value+percent initial",
        marker = {"color": ["#1E3A8A", "#3B82F6", "#60A5FA", "#93C5FD"]}
    ))
    
    fig.update_layout(
        title="Market Segmentation Funnel",
        showlegend=False,
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Pain points analysis
    st.subheader("🎯 Target Customer Pain Points")
    
    fig = px.bar(
        pain_points,
        x='Pain_Point',
        y='Prevalence',
        color='Priority',
        title='Top SMME Financial Pain Points',
        color_continuous_scale='Blues',
        text='Prevalence'
    )
    
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        xaxis_title="Pain Point",
        yaxis_title="Prevalence (%)",
        yaxis_range=[0, 50]
    )
    
    # Add Stoki addressing indicators
    for idx, row in pain_points.iterrows():
        if row['Addressed_by_Stoki']:
            fig.add_annotation(
                x=row['Pain_Point'],
                y=row['Prevalence'] + 2,
                text="✓ Addressed by Stoki",
                showarrow=False,
                font=dict(color="green", size=10)
            )
    
    st.plotly_chart(fig, use_container_width=True)

elif analysis_focus == "Competitive Landscape":
    st.header("⚔️ Competitive Intelligence")
    
    # Competitor comparison
    st.subheader("📈 Financial Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(
            competitors_data[competitors_data['Company'] != 'Stoki (Target)'],
            x='Company',
            y='Market_Share',
            color='YoY_Growth',
            title='Market Share & Growth',
            text='Market_Share',
            color_continuous_scale='RdYlGn'
        )
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig.update_layout(yaxis_title="Market Share (%)")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.scatter(
            competitors_data,
            x='ARPU_Monthly',
            y='CAC',
            size='Customers',
            color='Company',
            title='ARPU vs CAC (Bubble size = Customers)',
            hover_data=['Profit_Margin', 'CAC_Payback_Months']
        )
        
        # Add Stoki target line
        fig.add_hline(y=550, line_dash="dash", line_color="blue", 
                     annotation_text="Stoki Target CAC")
        fig.add_vline(x=349, line_dash="dash", line_color="blue",
                     annotation_text="Stoki Target ARPU")
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Feature gap analysis
    st.subheader("🔍 Feature Gap Analysis")
    # Melt features for heatmap
    features_melted = features.melt(id_vars=['Feature'], var_name='Company', value_name='Available')
    # Build a pivot table: rows = Features, columns = Companies, values = availability (0/1)
    feature_matrix = features.set_index('Feature').notna().astype(int)
    # Plot as heatmap
    fig = px.imshow(feature_matrix, labels=dict(x="Company", y="Feature", color="Available"), x=feature_matrix.columns,
    y=feature_matrix.index, color_continuous_scale='RdYlGn', aspect="auto", title="Competitive Feature Matrix")
    # Highlight Stoki column if present
    if 'Stoki' in feature_matrix.columns:fig.update_xaxes(tickangle=45, tickfont=dict(color="blue", size=12)
    )

       st.plotly_chart(fig, use_container_width=True)
    
    # Feature coverage statistics
    st.subheader("📊 Feature Coverage Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        stoki_coverage = features['Stoki'].sum() / len(features) * 100
        st.metric("Stoki Feature Coverage", f"{stoki_coverage:.0f}%", "7/7 features")
    
    with col2:
        avg_coverage = features.iloc[:, 1:-1].sum().sum() / (len(features) * (len(features.columns)-2)) * 100
        st.metric("Competitor Average", f"{avg_coverage:.0f}%", "4.3/7 features")
    
    with col3:
        st.metric("Stoki Advantage", f"{(stoki_coverage - avg_coverage):.0f}%", "+2.7 features")

elif analysis_focus == "Target Segmentation":
    st.header("🎯 Target Market Segmentation")
    
    # Segment comparison
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Market Size Distribution', 'Digital Adoption Rate', 
                       'ARPU Potential', 'CAC by Segment'),
        specs=[[{'type': 'pie'}, {'type': 'bar'}],
               [{'type': 'bar'}, {'type': 'bar'}]]
    )
    
    # Pie chart for market size
    fig.add_trace(
        go.Pie(labels=segments['Segment'], values=segments['Market_Size'], 
               name="Market Size", marker_colors=['#60A5FA', '#3B82F6', '#1D4ED8']),
        row=1, col=1
    )
    
    # Bar chart for digital adoption
    fig.add_trace(
        go.Bar(x=segments['Segment'], y=segments['Current_Digital_Adoption'],
               name="Digital Adoption", marker_color='#10B981'),
        row=1, col=2
    )
    
    # Bar chart for ARPU potential
    fig.add_trace(
        go.Bar(x=segments['Segment'], y=segments['ARPU_Potential'],
               name="ARPU Potential", marker_color='#F59E0B'),
        row=2, col=1
    )
    
    # Bar chart for CAC
    fig.add_trace(
        go.Bar(x=segments['Segment'], y=segments['CAC'],
               name="CAC", marker_color='#EF4444'),
        row=2, col=2
    )
    
    fig.update_layout(height=700, showlegend=False)
    fig.update_yaxes(title_text="Percentage", row=1, col=2)
    fig.update_yaxes(title_text="Rands", row=2, col=1)
    fig.update_yaxes(title_text="Rands", row=2, col=2)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Target segment rationale
    st.subheader("🎯 Why Target Small Businesses (11-50 employees)?")
    
    target_segment = segments.iloc[1]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Market Size", f"{target_segment['Market_Size']}%", "of total SMMEs")
    
    with col2:
        st.metric("Digital Adoption", f"{target_segment['Current_Digital_Adoption']}%", "ready to upgrade")
    
    with col3:
        st.metric("ARPU Potential", f"R{target_segment['ARPU_Potential']:,}", "/month")
    
    with col4:
        st.metric("Growth Rate", f"{target_segment['Growth_Rate']}%", "YoY")
    
    # Customer profile
    st.markdown('<div class="insight-box">', unsafe_allow_html=True)
    st.markdown("### 👥 Ideal Customer Profile")
    st.markdown("""
    - **Size:** 11-50 employees
    - **Revenue:** R5M - R50M annually
    - **Industry:** Professional services, retail, hospitality
    - **Pain Points:** Late payments, time-consuming admin, cash flow uncertainty
    - **Tech Savviness:** Digitally literate but time-poor
    - **Current Solution:** Using basic tools or dissatisfied with current provider
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif analysis_focus == "Positioning Strategy":
    st.header("🎯 Strategic Positioning")
    
    # Competitive positioning map
    st.subheader("🗺️ Competitive Positioning Map")
    
    # Create positioning map
    fig = px.scatter(
        positioning,
        x='X_Feature_Score',
        y='Y_Price_Index',
        size='Bubble_Size_Customers',
        color='Company',
        hover_data=['Quadrant'],
        title='Strategic Positioning: Feature Score vs Price Index',
        size_max=60
    )
    
    # Add quadrant lines
    fig.add_hline(y=5, line_dash="dash", line_color="gray", opacity=0.7)
    fig.add_vline(x=5, line_dash="dash", line_color="gray", opacity=0.7)
    
    # Add quadrant labels
    fig.add_annotation(x=3, y=8, text="Premium-Complex", showarrow=False, font=dict(size=10))
    fig.add_annotation(x=3, y=2, text="Budget-Basic", showarrow=False, font=dict(size=10))
    fig.add_annotation(x=8, y=8, text="Premium-Advanced", showarrow=False, font=dict(size=10))
    fig.add_annotation(x=8, y=2, text="Value-Advanced", showarrow=False, font=dict(size=10))
    
    # Highlight Stoki's target position
    fig.add_shape(type="circle",
        xref="x", yref="y",
        x0=8, y0=4.5, x1=9, y1=5.5,
        line=dict(color="blue", width=2, dash="dot"),
    )
    
    fig.update_layout(
        xaxis_title="Feature Score & Quality →",
        yaxis_title="Price Index →",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Value proposition
    st.subheader("💎 Stoki's Unique Value Proposition")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="strategy-card">', unsafe_allow_html=True)
        st.markdown("### 🎨 Beautiful UX")
        st.markdown("""
        - Intuitive interface
        - Mobile-first design
        - Easy onboarding
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="strategy-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Cashflow Automation")
        st.markdown("""
        - AI-powered forecasting
        - Automated payment reminders
        - Real-time insights
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="strategy-card">', unsafe_allow_html=True)
        st.markdown("### 🔄 All-in-One Solution")
        st.markdown("""
        - Invoicing + expenses
        - VAT ready
        - Bank integrations
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Pricing strategy
    st.subheader("💰 Pricing Strategy")
    
    pricing_data = pd.DataFrame({
        'Tier': ['Stoki Basic', 'Stoki Pro', 'Competitor Average', 'Market Leader'],
        'Price': [199, 349, 299, 599],
        'Features': ['Invoicing + Expenses', 'Full Suite + Cashflow', 'Limited Suite', 'Complex Suite']
    })
    
    fig = px.bar(
        pricing_data,
        x='Tier',
        y='Price',
        color='Tier',
        text='Price',
        title='Competitive Pricing Positioning',
        color_discrete_sequence=['#60A5FA', '#3B82F6', '#9CA3AF', '#6B7280']
    )
    
    fig.update_traces(texttemplate='R%{text}/month', textposition='outside')
    fig.update_layout(
        yaxis_title="Monthly Price (R)",
        showlegend=False
    )
    
    # Add value indicator
    fig.add_annotation(
        x='Stoki Pro',
        y=400,
        text="✓ Best Value",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        font=dict(color="green", size=12)
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif analysis_focus == "Performance Tracker":
    st.header("📊 Initial Performance Metrics")
    
    # Results dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Business Signups",
            f"{results.iloc[0]['Current']:,}",
            f"+{results.iloc[0]['Current'] - results.iloc[0]['Target']}",
            delta_color="normal"
        )
    
    with col2:
        mrr_target_achievement = (results.iloc[1]['Current'] / results.iloc[1]['Target']) * 100
        st.metric(
            "Monthly Recurring Revenue",
            f"R{results.iloc[1]['Current']:,}",
            f"{mrr_target_achievement:.0f}% of target"
        )
    
    with col3:
        cac_target_achievement = (results.iloc[2]['Target'] - results.iloc[2]['Current']) / results.iloc[2]['Target'] * 100
        st.metric(
            "Customer Acquisition Cost",
            f"R{results.iloc[2]['Current']:,}",
            f"{cac_target_achievement:.0f}% below target"
        )
    
    with col4:
        satisfaction = results.iloc[4]['Current']
        st.metric(
            "Customer Satisfaction",
            f"{satisfaction:.1f}/5.0",
            f"+{(satisfaction - 4.0)/4.0*100:.0f}%"
        )
    
    # Progress bars for key metrics
    st.subheader("📈 Progress Towards Targets")
    
    for idx, row in results.iterrows():
        progress = (row['Current'] / row['Target']) * 100 if row['Target'] > 0 else 0
        
        col1, col2, col3 = st.columns([2, 1, 3])
        
        with col1:
            st.markdown(f"**{row['Metric']}**")
        
        with col2:
            st.markdown(f"{row['Current']} {row['Unit']}")
        
        with col3:
            st.progress(min(progress/100, 1.0))
            st.caption(f"Target: {row['Target']} {row['Unit']} ({progress:.0f}%)")
    
    # Signups growth chart
    st.subheader("📈 Quarterly Growth Projection")
    
    growth_data = pd.DataFrame({
        'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
        'Signups': [217, 350, 500, 700],
        'MRR_R000': [75, 122, 175, 245],
        'CAC': [520, 480, 450, 420]
    })
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(x=growth_data['Quarter'], y=growth_data['Signups'], 
               name="Business Signups", marker_color='#3B82F6'),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(x=growth_data['Quarter'], y=growth_data['MRR_R000'], 
                  name="MRR (R'000)", mode='lines+markers', line=dict(color='#10B981', width=3)),
        secondary_y=True
    )
    
    fig.update_layout(
        title="Growth Projection - First Year",
        xaxis_title="Quarter",
        hovermode="x unified"
    )
    
    fig.update_yaxes(title_text="Business Signups", secondary_y=False)
    fig.update_yaxes(title_text="MRR (R'000)", secondary_y=True)
    
    st.plotly_chart(fig, use_container_width=True)

else:  # Go-to-Market Plan
    st.header("🚀 Go-to-Market Strategy")
    
    # Channel strategy
    st.subheader("🎯 Acquisition Channel Strategy")
    
    channels = pd.DataFrame({
        'Channel': ['Content Marketing', 'Accountant Partnerships', 'LinkedIn Ads', 
                   'SEO', 'Referral Program', 'Industry Events'],
        'CAC': [400, 300, 850, 200, 150, 1200],
        'Volume': ['High', 'Medium', 'Low', 'High', 'Medium', 'Low'],
        'Priority': [1, 1, 2, 1, 2, 3]
    })
    
    fig = px.scatter(
        channels,
        x='CAC',
        y='Priority',
        size=[30, 30, 20, 30, 20, 10],
        color='Volume',
        text='Channel',
        title='Channel Strategy: CAC vs Priority (Size = Investment Focus)',
        color_discrete_sequence=['#10B981', '#F59E0B', '#EF4444']
    )
    
    fig.update_traces(textposition='top center')
    fig.update_layout(
        xaxis_title="Customer Acquisition Cost (R)",
        yaxis_title="Priority (1 = Highest)",
        yaxis=dict(tickmode='array', tickvals=[1, 2, 3], ticktext=['High', 'Medium', 'Low'])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Product roadmap
    st.subheader("🛣️ Product Roadmap")
    
    roadmap = pd.DataFrame({
        'Phase': ['MVP Launch', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
        'Features': [
            'Core invoicing + basic reporting',
            'Expense tracking + VAT calculations',
            'Cashflow forecasting + bank integrations',
            'Advanced analytics + supplier payments'
        ],
        'Target Users': ['Early adopters', 'Small businesses', 'Growing SMBs', 'Established businesses'],
        'Status': ['✅ Completed', '🟡 In Progress', '🔜 Planned', '📅 Future']
    })
    
    for idx, row in roadmap.iterrows():
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col1:
            st.markdown(f"### {row['Phase']}")
        
        with col2:
            st.markdown(f"**{row['Features']}**")
            st.caption(f"Target: {row['Target Users']}")
        
        with col3:
            if row['Status'] == '✅ Completed':
                st.success(row['Status'])
            elif row['Status'] == '🟡 In Progress':
                st.warning(row['Status'])
            else:
                st.info(row['Status'])
        
        if idx < len(roadmap) - 1:
            st.markdown("---")
    
    # Implementation timeline
    st.subheader("📅 Implementation Timeline")
    
    timeline_data = pd.DataFrame({
        'Task': ['Market Research', 'MVP Development', 'Beta Testing', 
                'Channel Setup', 'Full Launch', 'Scale Operations'],
        'Start': ['2024-01-01', '2024-02-01', '2024-04-01', 
                 '2024-05-01', '2024-07-01', '2024-10-01'],
        'End': ['2024-01-31', '2024-03-31', '2024-06-30', 
               '2024-06-30', '2024-09-30', '2025-03-31'],
        'Status': ['Completed', 'Completed', 'In Progress', 
                  'In Progress', 'Planned', 'Planned']
    })
    
    timeline_data['Start'] = pd.to_datetime(timeline_data['Start'])
    timeline_data['End'] = pd.to_datetime(timeline_data['End'])
    
    fig = px.timeline(
        timeline_data, 
        x_start="Start", 
        x_end="End", 
        y="Task",
        color="Status",
        title="Implementation Timeline",
        color_discrete_map={
            'Completed': '#10B981',
            'In Progress': '#F59E0B',
            'Planned': '#60A5FA'
        }
    )
    
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=400)
    
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6B7280; padding: 2rem;'>
    <h3>🎯 Strategic Summary</h3>
    <p><strong>Target:</strong> Small businesses (11-50 employees) in major metros • 
    <strong>Price:</strong> R349/month • 
    <strong>Differentiator:</strong> Beautiful UX + Cashflow Automation</p>
    <p><strong>Goal:</strong> Capture 5% of SOM (2,000 businesses) in Year 1 • 
    <strong>MRR Target:</strong> R698,000/month • 
    <strong>Channels:</strong> Content marketing + Accountant partnerships</p>
    <small>Stoki Market Entry Dashboard • Last Updated: August 2024</small>
</div>
""", unsafe_allow_html=True)
