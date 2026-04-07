import streamlit as st
from openai import OpenAI

# 1. 界面设置
st.set_page_config(page_title="历史 AI 助手", layout="wide")
st.title("📜 历史学科 AI 深度解析系统")

# 2. 侧边栏配置 API (建议在这里填入 Key)
with st.sidebar:
    st.header("系统设置")
    api_key = st.text_input("输入你的 API Key", type="password")
    model_choice = st.selectbox("选择模型", ["deepseek-chat", "gpt-3.5-turbo"])
    st.info("提示：分析结果会自动生成下载按钮，方便您保存文档。")

# 3. 输入区
col_in1, col_in2 = st.columns(2)
with col_in1:
    question = st.text_area("请输入题目/史料内容：", height=200)
with col_in2:
    answer = st.text_area("请输入学生原始答案（选填）：", height=200)

# 4. 核心逻辑
if st.button("开始深度解构", type="primary"):
    if not api_key:
        st.error("请先在左侧输入 API Key！")
    else:
        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        
        with st.spinner("AI 正在解析材料..."):
            prompt = f"你是一位高三历史特级教师。请分析以下材料：\n{question}\n学生答案：{answer}\n\n请严格按以下三个板块输出：\n1.【材料解读】（分析时空背景与核心意图）\n2.【核心知识】（关联教材考点与阶段特征）\n3.【答题框架】（给出标准化得分逻辑）"
            
            response = client.chat.completions.create(
                model=model_choice,
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = response.choices[0].message.content
            st.markdown(result)
            
            # 5. 保存功能：提供下载按钮
            st.download_button(
                label="📥 下载本次分析报告",
                data=result,
                file_name="历史错题分析.txt",
                mime="text/plain"
            )
