# history-ai-tool
import streamlit as st

# 页面配置
st.set_page_config(page_title="历史 AI 智能错题本", layout="wide")

st.title("📜 历史学科 AI 错题深度分析系统")
st.markdown("---")

# 侧边栏：输入区域
with st.sidebar:
    st.header("错题输入")
    subject_module = st.selectbox("所属模块", ["中外历史纲要(上)", "中外历史纲要(下)", "选择性必修"])
    question_text = st.text_area("输入题目/材料内容", height=200, placeholder="粘贴题目材料或手打内容...")
    student_answer = st.text_area("学生原始答案", height=150)
    analyze_btn = st.button("开始 AI 深度解构", type="primary")

# 主界面：深度分析输出
if analyze_btn and question_text:
    # 模拟 AI 处理后的结构化数据
    # 实际应用中，这里会调用 OpenAI/DeepSeek 的 API 接口
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🔍 材料解读")
        st.success("**关键信息点提取：**")
        st.write("1. **时间节点**：19 世纪末 20 世纪初（世纪之交）。")
        st.write("2. **核心要素**：民族资本主义、清末新政、实业救国。")
        st.write("3. **隐性信息**：材料折射出社会转型时期的矛盾与动能。")

    with col2:
        st.subheader("💡 核心知识")
        st.warning("**教材关联与重难点：**")
        st.markdown("""
        - **必备知识**：中国民族资本主义的发展阶段（短暂春天）。
        - **关键概念**：早期现代化、阶级结构变动。
        - **高考考向**：常与西方工业文明冲击、晚清政治变革相结合。
        """)

    with col3:
        st.subheader("🏗️ 答题框架")
        st.info("**规范化论证逻辑：**")
        st.markdown("""
        **[原因/背景类提纲]**
        1. **经济层**：自然经济瓦解，商品经济发展。
        2. **政治层**：清政府政策调整或民族危机加深。
        3. **思想层**：维新思想或民主革命思想的传播。
        4. **外部层**：第二次工业革命的影响。
        """)

    st.markdown("---")
    st.subheader("📈 错题纠偏建议")
    st.error(f"**诊断结果**：你的答案偏重于描述现象，缺乏“{subject_module}”要求的政治/经济/文化三位一体分析法。建议加强对阶段特征的记忆。")
    
    if st.button("保存至我的永久错题库"):
        st.toast("已成功存入数据库，支持一键导出空白练习卷！")
