import random
import pygame
pygame.init()


LEFT_EYE_MARKS = [246,161,160,159,158,157,173,133,155,154,153,145,144,163,7,33]
RIGHT_EYE_MARKS = [384,385,386,387,388,466,559,555,390,373,374,380,381,382,398]
HAND_LINE_COLOR = (0,255,127)
HAND_LINE_SIZE = 6
HAND_CIRCLE_COLOR = (0,255,127)
HAND_CIRCLE_SIZE = 3

				
def DrawHands(screen,hand):
	for hm in hand.multi_hand_landmarks:
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[0].x*screen.get_width()),int(hm.landmark[0].y*screen.get_height())),(int(hm.landmark[1].x*screen.get_width()),int(hm.landmark[1].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[1].x*screen.get_width()),int(hm.landmark[1].y*screen.get_height())),(int(hm.landmark[2].x*screen.get_width()),int(hm.landmark[2].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[2].x*screen.get_width()),int(hm.landmark[2].y*screen.get_height())),(int(hm.landmark[3].x*screen.get_width()),int(hm.landmark[3].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[3].x*screen.get_width()),int(hm.landmark[3].y*screen.get_height())),(int(hm.landmark[4].x*screen.get_width()),int(hm.landmark[4].y*screen.get_height())),HAND_LINE_SIZE)
		
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[5].x*screen.get_width()),int(hm.landmark[5].y*screen.get_height())),(int(hm.landmark[6].x*screen.get_width()),int(hm.landmark[6].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[6].x*screen.get_width()),int(hm.landmark[6].y*screen.get_height())),(int(hm.landmark[7].x*screen.get_width()),int(hm.landmark[7].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[7].x*screen.get_width()),int(hm.landmark[7].y*screen.get_height())),(int(hm.landmark[8].x*screen.get_width()),int(hm.landmark[8].y*screen.get_height())),HAND_LINE_SIZE)

		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[9].x*screen.get_width()),int(hm.landmark[9].y*screen.get_height())),(int(hm.landmark[10].x*screen.get_width()),int(hm.landmark[10].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[10].x*screen.get_width()),int(hm.landmark[10].y*screen.get_height())),(int(hm.landmark[11].x*screen.get_width()),int(hm.landmark[11].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[11].x*screen.get_width()),int(hm.landmark[11].y*screen.get_height())),(int(hm.landmark[12].x*screen.get_width()),int(hm.landmark[12].y*screen.get_height())),HAND_LINE_SIZE)
		
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[13].x*screen.get_width()),int(hm.landmark[13].y*screen.get_height())),(int(hm.landmark[14].x*screen.get_width()),int(hm.landmark[14].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[14].x*screen.get_width()),int(hm.landmark[14].y*screen.get_height())),(int(hm.landmark[15].x*screen.get_width()),int(hm.landmark[15].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[15].x*screen.get_width()),int(hm.landmark[15].y*screen.get_height())),(int(hm.landmark[16].x*screen.get_width()),int(hm.landmark[16].y*screen.get_height())),HAND_LINE_SIZE)

		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[17].x*screen.get_width()),int(hm.landmark[17].y*screen.get_height())),(int(hm.landmark[18].x*screen.get_width()),int(hm.landmark[18].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[18].x*screen.get_width()),int(hm.landmark[18].y*screen.get_height())),(int(hm.landmark[19].x*screen.get_width()),int(hm.landmark[19].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[19].x*screen.get_width()),int(hm.landmark[19].y*screen.get_height())),(int(hm.landmark[20].x*screen.get_width()),int(hm.landmark[20].y*screen.get_height())),HAND_LINE_SIZE)

		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[5].x*screen.get_width()),int(hm.landmark[5].y*screen.get_height())),(int(hm.landmark[9].x*screen.get_width()),int(hm.landmark[9].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[9].x*screen.get_width()),int(hm.landmark[9].y*screen.get_height())),(int(hm.landmark[13].x*screen.get_width()),int(hm.landmark[13].y*screen.get_height())),HAND_LINE_SIZE)
		pygame.draw.line(screen,HAND_LINE_COLOR,(int(hm.landmark[13].x*screen.get_width()),int(hm.landmark[13].y*screen.get_height())),(int(hm.landmark[17].x*screen.get_width()),int(hm.landmark[17].y*screen.get_height())),HAND_LINE_SIZE)

		for m in hm.landmark:
			pygame.draw.circle(screen,HAND_CIRCLE_COLOR,(m.x*screen.get_width(),m.y*screen.get_height()),HAND_CIRCLE_SIZE)


def DrawAvatar(screen,resoult,effective=None):
	for face_l in resoult.multi_face_landmarks:
		pygame.draw.line(screen,(0,200,200),(face_l.landmark[187].x*screen.get_width(),face_l.landmark[187].y*screen.get_height()),(face_l.landmark[182].x*screen.get_width(),face_l.landmark[182].y*screen.get_height()),5)
		pygame.draw.line(screen,(0,200,200),(face_l.landmark[411].x*screen.get_width(),face_l.landmark[411].y*screen.get_height()),(face_l.landmark[406].x*screen.get_width(),face_l.landmark[406].y*screen.get_height()),5)
		pygame.draw.line(screen,(0,200,200),(face_l.landmark[116].x*screen.get_width(),face_l.landmark[116].y*screen.get_height()),(face_l.landmark[70].x*screen.get_width(),face_l.landmark[70].y*screen.get_height()),5)
		pygame.draw.line(screen,(0,200,200),(face_l.landmark[346].x*screen.get_width(),face_l.landmark[346].y*screen.get_height()),(face_l.landmark[276].x*screen.get_width(),face_l.landmark[276].y*screen.get_height()),5)
		pygame.draw.line(screen,(0,200,200),(face_l.landmark[70].x*screen.get_width(),face_l.landmark[70].y*screen.get_height()),(face_l.landmark[67].x*screen.get_width(),face_l.landmark[67].y*screen.get_height()),5)
		pygame.draw.line(screen,(0,200,200),(face_l.landmark[276].x*screen.get_width(),face_l.landmark[276].y*screen.get_height()),(face_l.landmark[297].x*screen.get_width(),face_l.landmark[297].y*screen.get_height()),5)
	
		if effective != None:
			effective.x = [face_l.landmark[187].x*screen.get_width(),face_l.landmark[411].x*screen.get_width()]
			effective.y = face_l.landmark[182].y*screen.get_height()
		
		# pygame.draw.line(screen,(0,255,255),(face_l.landmark[67].x*screen.get_width(),face_l.landmark[67].y*screen.get_height()),(face_l.landmark[9].x*screen.get_width(),face_l.landmark[9].y*screen.get_height()),5)
		# pygame.draw.line(screen,(0,255,255),(face_l.landmark[297].x*screen.get_width(),face_l.landmark[297].y*screen.get_height()),(face_l.landmark[9].x*screen.get_width(),face_l.landmark[9].y*screen.get_height()),5)
		
		for id,mark in enumerate(face_l.landmark):
			if id in RIGHT_EYE_MARKS:
				x,y = int(mark.x*screen.get_width()),int(mark.y*screen.get_height())
				# cv2.circle(img,(x,y),1,(0,0,255),)
				ol,ox,oy = 0,0,0
				for ii in RIGHT_EYE_MARKS:
					try:
						tx,ty = int(face_l.landmark[ii].x*screen.get_width()),int(face_l.landmark[ii].y*screen.get_height())
						ox+=tx
						oy+=ty
						ol+=1
						pygame.draw.line(screen,(200,200,200),(x,y),(tx,ty),1)			
					except:
						pass
				# pygame.draw.circle(screen,(0,0,0),(int(ox/ol),int(oy/ol)),5)
				pygame.draw.circle(screen,(0,255,127),(x,y),3)
			if id in LEFT_EYE_MARKS: #or id in RIGHT_EYE_MARKS:
				x,y = int(mark.x*screen.get_width()),int(mark.y*screen.get_height())
				# cv2.circle(img,(x,y),1,(0,0,255),)
				ol,ox,oy = 0,0,0
				for i in LEFT_EYE_MARKS:
					tx,ty = int(face_l.landmark[i].x*screen.get_width()),int(face_l.landmark[i].y*screen.get_height())
					ox+=tx
					oy+=ty
					ol+=1
					pygame.draw.line(screen,(255,255,255),(x,y),(tx,ty),1)							# pygame.draw.circle(screen,(0,0,0),(int(ox/ol),int(oy/ol)),5)
				pygame.draw.circle(screen,(0,255,100),(x,y),3)