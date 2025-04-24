import torch
import torch.nn as nn
import torch.nn.functional as F

def channel_shuffle(x, groups):
	batchsize, num_channels, height, width = x.data.size()

	channels_per_group = num_channels // groups
    
	# reshape
	x = x.view(batchsize, groups, channels_per_group, height, width)

	x = torch.transpose(x, 1, 2).contiguous()

	# flatten
	x = x.view(batchsize, -1, height, width)

	return x

class Parsimonious_Conv(nn.Module):

	def __init__(self, inChannels, outChannels, p, m, s):
		super(Parsimonious_Conv, self).__init__()
		self.inChannels = inChannels
		self.split = p
		self.inChannelsforkelsize3 = inChannels//p	
		self.multichannels = self.inChannelsforkelsize3//m
		self.inChannelsforkelsize1 = inChannels - self.inChannelsforkelsize3
		
		self.conv1 = nn.Conv2d(self.inChannelsforkelsize3, self.multichannels, kernel_size=1, stride=1, padding=0, groups=1)
		self.bn1 = nn.BatchNorm2d(self.multichannels)		
		
		self.conv1_1 = nn.Conv2d(self.multichannels, self.multichannels, kernel_size=3, stride=s, padding=1,groups=self.multichannels)
		self.bn1_1 = nn.BatchNorm2d(self.multichannels)
		
		self.conv1_2 = nn.Conv2d(self.multichannels, outChannels, kernel_size=1, stride=1, padding=0, groups=1)

		self.conv2 = nn.Conv2d(self.inChannelsforkelsize1, outChannels, kernel_size=1, stride=s, padding=0)
		self.bn2 = nn.BatchNorm2d(outChannels)

	def forward(self, x):
		new_x = channel_shuffle(x, self.split)
		x1 = new_x[:,0:self.inChannelsforkelsize3,:,:]
		x2 = new_x[:,(self.inChannelsforkelsize3):(self.inChannels),:,:]
		out1 = self.bn1(self.conv1(x1))
		out1 = self.bn1_1(self.conv1_1(out1))
		out1 = self.conv1_2(out1)	
		out2 = self.conv2(x2)
		out = torch.add(out1,out2)
		out = self.bn2(out)
		out = F.relu(out)
		return out

class Example_ParNN(nn.Module):
    def __init__(self, in_channel):
        super(Example_ParNN, self).__init__()

        #Par_Block
        self.b1_c1 = Parsimonious_Conv(in_channel,64,2,2,1)

    def forward(self, x):

        out = self.b1_c1(x)

        return out