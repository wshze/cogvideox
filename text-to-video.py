import time
from zhipuai import ZhipuAI

# 请填写您自己的APIKey
api_key = "ef6798eeGJNRxxxxxxxxxxxxxxxxxxxxxxxxxx"
client = ZhipuAI(api_key=api_key)

# 获取用户输入的提示内容
prompt = input("请输入视频生成的提示内容：")

generation_response = client.videos.generations(
    model="cogvideox",
    prompt=prompt
)
#print("Generation Response:", generation_response)

# 获取视频任务ID
video_id = generation_response.id

# 输出 video_id 的值
#print(f"视频ID为: {video_id}")

# 查询视频生成状态
while True:
    result_response = client.videos.retrieve_videos_result(id=video_id)
    
    if result_response.task_status == 'PROCESSING':
        print('视频生成中。请稍候...')
        time.sleep(10)  # 每隔10秒检查一次
    elif result_response.task_status == 'SUCCESS':
        break
    else:
        print(f'异常: {result_response.task_status}')
        break

# 查看返回结果，调试用
#print("Result Response:", result_response)

# 提取视频URL地址
if result_response.video_result:
    video_url = result_response.video_result[0].url
    print(f"视频生成成功，下载地址为: {video_url}")
else:
    print("未找到视频url地址.")
